import urwid
import os

def handle_input(key):
	if key == 'q' or key == 'Q':
		raise urwid.ExitMainLoop()

def getFolders(cur_dir):
	body = [urwid.Text('Current directory: ' + cur_dir), urwid.Divider()]
	folders = [folder for folder in os.listdir(cur_dir) if os.path.isdir(os.path.join(cur_dir, folder))]
	for f in folders:
		button = urwid.Button(f)
		f = '"%s"' % f if ' ' in f else f
		urwid.connect_signal(button, 'click', item_chosen, user_args=[cur_dir + '/' + f])
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def getBackups():
	return menu(u'backup', ['aaa'])
	body = [urwid.Text(title), urwid.Divider()]
	for c in choices:
		button = urwid.Button(c)
		urwid.connect_signal(button, 'click', item_chosen, user_args=[c])
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def menu(title, choices):
	body = [urwid.Text(title), urwid.Divider()]
	for c in choices:
		button = urwid.Button(c)
		urwid.connect_signal(button, 'click', item_chosen, user_args=[c])
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def genTips():
	tips_text = "Tips:\nq\t:\tquit"
	body = [urwid.Text(tips_text), urwid.Divider()]
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, folder):
	main.original_widget = getFolders(folder)

def exit_program(button):
	raise urwid.ExitMainLoop()

file_structure = [
	"Folder Structure:",
	"- File1",
	"- File2",
	"- Directory1",
	"  - Subfile1",
	"  - Subfile2"
]

left_top = getFolders("/mnt/c/Users/hebel/DownLoads")
left_middle = getBackups()
left_bottom = genTips()
right = urwid.ListBox(urwid.SimpleFocusListWalker([urwid.Text(line) for line in file_structure]))

left_top_box = urwid.LineBox(left_top, title="Folders")
left_middle_box = urwid.LineBox(left_middle, title="Backups")
left_bottom_box = urwid.LineBox(left_bottom, title="tips")
right_box = urwid.LineBox(right, title="Folder Structure")

# 主界面組裝
left_column = urwid.Pile([left_top_box, left_middle_box, left_bottom_box])
main = urwid.Columns([left_column, right_box])

top = urwid.Frame(main, header=urwid.Text(u"LazyChangeCode"))
mainloop = urwid.MainLoop(top, palette=[('reversed', 'standout', '')], unhandled_input=handle_input)
mainloop.run()
