class TreeNode():
    '''
    创建树节点，同时为了遍历创建一个访问变量
    '''
    def __init__(self, data):
        self.data = data
        self.visited = False

    def __str__(self):
        return str(self.data)

    def sonNode(self, left, right):
        self.left = TreeNode(None)
        self.right = TreeNode(None)
        self.left.data = left
        self.right.data = right


class TreeMethods():
    def makeselfTree(self, point: TreeNode, limit: int):
        '''
        创建一个以自身构造的树
        :param point: inital root point
        :param limit: the depth of the tree
        :return:
        '''
        locallimit = limit
        if locallimit == 1:
            point.sonNode(None, None)
        else:
            point.sonNode('(',')')
            locallimit -= 1
            self.makeselfTree(point.left, locallimit)
            self.makeselfTree(point.right, locallimit)

    def traversalTree(self, head: TreeNode):
        '''
        Use DFS to traverse the tree
        :param head: the root point of tree
        :return:
        '''
        self.candidate = []
        stack = []
        data = []
        stack.append(head)
        head.visited = True
        while stack != []:
            currentpoint = stack[-1]
            if currentpoint.left.data == None:
                self.candidate.append("".join([x.data for x in stack]))
                stack = stack[:-1]
            elif False in [currentpoint.left.visited, currentpoint.right.visited]:
                for i in [currentpoint.left, currentpoint.right]:
                    if i.visited == False:
                        i.visited =True
                        stack.append(i)
                        break
            else:
                stack = stack[:-1]


class Solution:
    def generateParenthesis(self, n: int):
        root_point = TreeNode('(')
        MakeTree = TreeMethods()
        MakeTree.makeselfTree(root_point, 3)
        MakeTree.traversalTree(root_point)
        print(MakeTree.candidate)




if __name__ == "__main__":
    S = Solution()
    S.generateParenthesis(6)