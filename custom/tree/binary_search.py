#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  15:31


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def has_value(self, value):
        return True if self.value == value else False


class BST(object):

    def __init__(self, datas):
        self.root = Node(datas[0])
        for data in datas[1:]:
            self.insert(data)
        self.q = []

    def search(self, node, value, parent):
        """

        :param node: 当前节点
        :param value: 值
        :param parent: 父节点
        :return:
        """
        if not node:
            return False, node, parent
        elif node.value == value:
            return True, node, parent
        elif node.value < value:
            return self.search(node.right, value, node)
        else:
            return self.search(node.left, value, node)

    def insert(self, value):
        flag, node, parent = self.search(self.root, value, self.root)
        new_node = Node(value)
        if not flag:
            if parent.value > value:
                parent.left = new_node
            else:
                parent.right = new_node

    def delete(self, data):
        flag, node, parent = self.search(self.root, data, self.root)
        if flag:
            if not node.left and not node.right:
                if parent.right is node:
                    # 直接将父节点指向空即可
                    parent.right = None
                else:
                    parent.left = None
                del_node = node
            elif node.left and not node.right:
                if parent.right is node:
                    parent.right = node.left
                else:
                    parent.left = node.left
                del_node = node
            elif node.left and node.right:
                del_node = self.min(node)
                flag, _, parent = self.search(node, del_node.value, node)
                if parent.right is del_node:
                    parent.right = None
                else:
                    parent.left = None
                node.value = del_node.value
            else:
                del_node = None
            return del_node
        return

    def delete_min(self):
        min_value = self.min(self.root).value
        flag, node, parent = self.search(self.root, min_value, self.root)
        parent.left = node.right
        return node

    def delete_max(self):
        max_value = self.max(self.root).value
        flag, node, parent = self.search(self.root, max_value, self.root)
        parent.right = node.left
        return node

    def pre_order_traverse(self, node):
        if node is not None:
            print node.value,
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)

    def level_queue(self):
        node = self.root
        self.q.append(node)
        while self.q:
            node = self.q.pop(0)
            if not node:
                break
            print(node.value)
            if node.left:
                self.q.append(node.left)
            if node.right:
                self.q.append(node.right)

    def min(self, node):
        if node.left:
            node = node.left
        else:
            return node
        return self.min(node)

    def max(self, node):
        if node.right:
            node = node.right
        else:
            return node
        return self.max(node)


if __name__ == '__main__':
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 2]
    bst = BST(a)
    # print(bst.preOrderTraverse(bst.root))
    # print(bst.level_queue())
    # print(bst.max(bst.root).value)
    print(bst.delete_min())
    print(bst.pre_order_traverse(bst.root))
    print(bst.delete_max())
    print(bst.pre_order_traverse(bst.root))
    print(bst.delete(13))
    print(bst.pre_order_traverse(bst.root))
