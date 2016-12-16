import sublime
import sublime_plugin
import time
date_time_format     = "%Y-%m-%d %H:%M:%S"            # 2013-10-02
time_format     = "%H:%M:%S"            # 10:24:01
stamp_format    = "%y%m%d%H%M%S"        # 131002102355
version_format  = "v%Y.%m.%d.%H.%M.%S"  # v2013.10.02.10.23.52
version_pattern = "v[0-9]{4}\.[0-9]{2}\.[0-9]{2}\.[0-9]{2}\.[0-9]{2}\.[0-9]{2}"
class towebu_insert_versionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            if not self.view.find_all(version_pattern):
                self.view.replace(edit, sel, time.strftime(version_format));
                return
            region = sublime.Region(0, self.view.size())
        results = self.view.find_all(version_pattern)
        for result in results:
            self.view.replace(edit, result, time.strftime(version_format))
class towebu_insert_stampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(stamp_format));
class towebu_insert_dateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(date_time_format));
class towebu_insert_timeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            self.view.replace(edit, sel, time.strftime(time_format));