import sys

class FileTree:
    def __init__(self):
        self.file_tree = {}
    
    def process_all(self, cli_list):
        for item in cli_list:
            act = item[0]
            if act == "mkdir":
                self._mkdir(item[1])
            elif act == "rm":
                self._rm(item[1])
            elif act == 'mv':
                self._mv(item[1], item[2])
            elif act == 'ls':
                self._ls()
            else:
                break

    @staticmethod
    def split_path(path):
        temp = path.split('/')
        return [i for i in temp if i]
    
    def _mkdir(self, path):
        dir_list = self.split_path(path)
        parent = self.file_tree
        level = 0
        while level < len(dir_list):
            cur = dir_list[level]
            if cur not in parent:
                parent[cur] = {}
            parent = parent[cur]
            level += 1
        print(parent)

    
    def _rm(self, path):
        dir_list = self.split_path(path)
        parent = self.file_tree
        level = 0
        while level < len(dir_list)-1:
            cur = dir_list[level]
            if cur not in parent:
                parent[cur] = {}
            parent = parent[cur]
            level += 1
            try:
                del parent[dir_list[-1]]
            except AttributeError:
                print('del Error')
                pass
    
    def _check_path_exit(self, path):
        dir_list = self.split_path(path)
        parent = self.file_tree
        level = 0
        while level < len(dir_list):
            cur = dir_list[level]
            if cur not in parent:
                return False
            parent = parent[cur]
            level += 1
        return True
    
    def _mv(self, path_from, path_to):
        if not self._check_path_exit(path_from):
            return 
        mv_parent = path_to[:path_to.rfind('/')]
        if path_to != '/' and not self._check_path_exit(mv_parent):
            return
        if path_to.find(path_from) == 0 or path_from.find(path_to) == 0:
            return
        if self._check_path_exit(path_to):
            return
        self._mkdir(path_to)
        self._rm(path_from)

    def _ls(self):
        res = ['/']

        def dfs_helper(last_dir, cur_level):
            for k, v in cur_level.items():
                cur_path = last_dir + '/' + k
                res.append(cur_path)
                dfs_helper(cur_path, v)
            dfs_helper('', self.file_tree)
            res.sort()
            for s in res:
                print(s)

if __name__ == "__main__":
    str_list =[]
    for line in sys.stdin:
        cur_line = list(line.split())
        str_list.append(cur_line)
    sys_tree = FileTree()
    sys_tree.process_all(str_list)