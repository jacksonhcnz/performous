from pathlib import Path

import plistlib

#
# Example settings file for dmgbuild
#

# Use like this: dmgbuild -s settings.py "Test Volume" test.dmg

# You can actually use this file for your own application (not just TextEdit)
# by doing e.g.
#
#	dmgbuild -s settings.py -D app=/path/to/My.app "My Application" MyApp.dmg

# .. Useful stuff ..............................................................
app_string = defines.get('app', '../Performous.app')
application = Path(app_string)

if app_string[0] == "~":
	application = application.expanduser()
application = application.resolve()

appname = application.name

def icon_from_app(app_path):
	plist_path = (app_path / 'Contents/Info.plist').resolve()
	with open(plist_path, 'rb') as f:
		plist = plistlib.load(f)
	icon_name = Path(plist['CFBundleIconFile'])
	if not icon_name.suffix:
		icon_name = icon_name.with_suffix('icns')
	return str(app_path / 'Contents/Resources' / icon_name)


# .. Basics ....................................................................

# Uncomment to override the output filename
# filename = 'test.dmg'

# Uncomment to override the output volume name
# volume_name = 'Test'

# Volume format (see hdiutil create -help)
format = defines.get('format', 'UDZO')	# noqa: F821

# Compression level (if relevant)
# compression_level = 9

# Volume size
size = defines.get('size', None)  # noqa: F821

# Files to include
files = [str(application.resolve())]

# Symlinks to create
symlinks = {'Applications': '/Applications'}

# Files to hide
hide = [ '' ]

# Files to hide the extension of
# hide_extension = [ 'README.rst' ]

# Volume icon
#
# You can either define icon, in which case that icon file will be copied to the
# image, *or* you can define badge_icon, in which case the icon file you specify
# will be used to badge the system's Removable Disk icon. Badge icons require
# pyobjc-framework-Quartz.
#
icon = icon_from_app(application)
# badge_icon = icon_from_app(application)

# .. Window configuration ......................................................

# Background
#
# This is a STRING containing any of the following:
#
#	 #3344ff		  - web-style RGB color
#	 #34f			  - web-style RGB color, short form (#34f == #3344ff)
#	 rgb(1,0,0)		  - RGB color, each value is between 0 and 1
#	 hsl(120,1,.5)	  - HSL (hue saturation lightness) color
#	 hwb(300,0,0)	  - HWB (hue whiteness blackness) color
#	 cmyk(0,1,0,0)	  - CMYK color
#	 goldenrod		  - X11/SVG named color
#	 builtin-arrow	  - A simple built-in background with a blue arrow
#	 /foo/bar/baz.png - The path to an image file
#
# The hue component in hsl() and hwb() may include a unit; it defaults to
# degrees ('deg'), but also supports radians ('rad') and gradians ('grad'
# or 'gon').
#
# Other color components may be expressed either in the range 0 to 1, or
# as percentages (e.g. 60% is equivalent to 0.6).
background = defines.get('background', './resources/dmg-bg.png')

show_status_bar = False
show_tab_view = False
show_toolbar = False
show_pathbar = False
show_sidebar = False
sidebar_width = 0

# Window position in ((x, y), (w, h)) format
window_rect = ((50, 50), (781, 643))

# Where to put the icons
icon_locations = {
	appname:		(221, 296),
	'Applications': (592, 296),
	'.background.tiff': (570,475),
	'.DS_Store': (150,475),
	'.VolumeIcon.icns': (410,475)
}

# Select the default view; must be one of
#
#	 'icon-view'
#	 'list-view'
#	 'column-view'
#	 'coverflow'
#
default_view = 'icon-view'

# General view configuration
show_icon_preview = False

# Set these to True to force inclusion of icon/list view settings (otherwise
# we only include settings for the default view)
include_icon_view_settings = True
include_list_view_settings = False

# .. Icon view configuration ...................................................

arrange_by = None
grid_offset = (0, 0)
grid_spacing = 100
scroll_position = (0, 0)
label_pos = 'bottom'  # or 'right'
text_size = 16
icon_size = 128

# .. List view configuration ...................................................

# Column names are as follows:
#
#	name
#	date-modified
#	date-created
#	date-added
#	date-last-opened
#	size
#	kind
#	label
#	version
#	comments
#
list_icon_size = 16
list_text_size = 12
list_scroll_position = (0, 0)
list_sort_by = 'name'
list_use_relative_dates = True
list_calculate_all_sizes = False,
list_columns = ('name', 'date-modified', 'size', 'kind', 'date-added')
list_column_widths = {
	'name': 300,
	'date-modified': 181,
	'date-created': 181,
	'date-added': 181,
	'date-last-opened': 181,
	'size': 97,
	'kind': 115,
	'label': 100,
	'version': 75,
	'comments': 300,
	}
list_column_sort_directions = {
	'name': 'ascending',
	'date-modified': 'descending',
	'date-created': 'descending',
	'date-added': 'descending',
	'date-last-opened': 'descending',
	'size': 'descending',
	'kind': 'ascending',
	'label': 'ascending',
	'version': 'ascending',
	'comments': 'ascending',
	}

# .. License configuration .....................................................

# Text in the license configuration is stored in the resources, which means
# it gets stored in a legacy Mac encoding according to the language.  dmgbuild
# will *try* to convert Unicode strings to the appropriate encoding, *but*
# you should be aware that Python doesn't support all of the necessary encodings;
# in many cases you will need to encode the text yourself and use byte strings
# instead here.

license = {
	'default-language': 'en_US',
	'licenses': {
		# For each language, the text of the license.  This can be plain text,
		# RTF (in which case it must start "{\rtf1"), or a path to a file
		# containing the license text.	If you're using RTF,
		# watch out for Python escaping (or read it from a file).
		'en_US': '../LICENSE.md',
	},
}
