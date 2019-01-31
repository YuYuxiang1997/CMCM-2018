# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:54:51 2018

@author: pengu
"""
import unittest

class Node:
    def __init__(self,coordinate,edges):
        self.coord = coordinate
        self.edges = edges
        
    def output(self):
        output = []
        for i in range(len(self.edges)):
            if self.edges[i].out1 is self:
                output.append[self.edges[i].out2]
            else:
                output.append[self.edges[i].out1]
        return output
    
class Edge:
    def __init__(self,node1,node2,length):
        self.out1 = node1
        self.out2 = node2
        self.length = length

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,edge):
        self.edges.append(edge)
        edge.out1.edges.append(edge)
        edge.out2.edges.append(edge)

def get_node(x,y):
    for i in range(len(graph.nodes)):
        if (x,y) == graph.nodes[i].coord:
            return graph.nodes[i]

def dijsktra(graph, initial, end):
    frontier = {initial:0}
    settled = []
    while len(frontier) != 0:
        a_min = min(frontier.values())
        a_node =0
        for j in frontier:
            if frontier[j]==a_min:
                a_node = j
                break
        if a_node is end:
            return a_min
        del frontier[a_node]
        settled.append(a_node)
        for i in range(len(a_node.edges)):
            b_edge = a_node.edges[i]
            if b_edge.out1 is a_node:
                b_node = b_edge.out2
            else:
                b_node = b_edge.out1
            if b_node not in settled:
                if b_node not in frontier.keys():
                    frontier.update({b_node:(a_min+b_edge.length)})
                elif (a_min+b_edge.length) < frontier[b_node]:
                    frontier[b_node] = a_min+b_edge.length
            
#    while nodes: 
#        min_node = None
#        for node in nodes:
#            if node in visited:
#                if min_node is None:
#                    min_node = node
#                elif visited[node] < visited[min_node]:
#                    min_node = node
#
#        if min_node is None:
#            break
#
#        nodes.remove(min_node)
#        current_weight = visited[min_node]
#
#        for edge in graph.edges[min_node]:
#            weight = current_weight + graph.distance[(min_node, edge)]
#            if edge not in visited or weight < visited[edge]:
#                visited[edge] = weight
#                path[edge] = min_node
#
#    return visited, path
        
graph = Graph()
n11 = Node((1,1),[])
graph.add_node(n11)
n12 = Node((1,2),[])
graph.add_node(n12)
n13 = Node((1,3),[])
graph.add_node(n13)
n14 = Node((1,4),[])
graph.add_node(n14)
n15 = Node((1,5),[])
graph.add_node(n15)
n16 = Node((1,6),[])
graph.add_node(n16)
n21 = Node((2,1),[])
graph.add_node(n21)
n22 = Node((2,2),[])
graph.add_node(n22)
n23 = Node((2,3),[])
graph.add_node(n23)
n24 = Node((2,4),[])
graph.add_node(n24)
n25 = Node((2,5),[])
graph.add_node(n25)
n26 = Node((2,6),[])
graph.add_node(n26)
n31 = Node((3,1),[])
graph.add_node(n31)
n32 = Node((3,2),[])
graph.add_node(n32)
n33 = Node((3,3),[])
graph.add_node(n33)
n34 = Node((3,4),[])
graph.add_node(n34)
n35 = Node((3,5),[])
graph.add_node(n35)
n36 = Node((3,6),[])
graph.add_node(n36)
n41 = Node((4,1),[])
graph.add_node(n41)
n42 = Node((4,2),[])
graph.add_node(n42)
n43 = Node((4,3),[])
graph.add_node(n43)
n44 = Node((4,4),[])
graph.add_node(n44)
n45 = Node((4,5),[])
graph.add_node(n45)
n46 = Node((4,6),[])
graph.add_node(n46)
n51 = Node((5,1),[])
graph.add_node(n51)
n52 = Node((5,2),[])
graph.add_node(n52)
n53 = Node((5,3),[])
graph.add_node(n53)
n54 = Node((5,4),[])
graph.add_node(n54)
n55 = Node((5,5),[])
graph.add_node(n55)
n56 = Node((5,6),[])
graph.add_node(n56)
n61 = Node((6,1),[])
graph.add_node(n61)
n62 = Node((6,2),[])
graph.add_node(n62)
n63 = Node((6,3),[])
graph.add_node(n63)
n64 = Node((6,4),[])
graph.add_node(n64)
n65 = Node((6,5),[])
graph.add_node(n65)
n66 = Node((6,6),[])
graph.add_node(n66)
e2132 = Edge(n21,n32,72)
graph.add_edge(e2132)
e2131 = Edge(n21,n31,60)
graph.add_edge(e2131)
e3141 = Edge(n31,n41,84)
graph.add_edge(e3141)
e4142 = Edge(n41,n42,36)
graph.add_edge(e4142)
e3242 = Edge(n32,n42,60)
graph.add_edge(e3242)
e1222 = Edge(n12,n22,90)
graph.add_edge(e1222)
e2242 = Edge(n22,n42,120)
graph.add_edge(e2242)
e4251 = Edge(n42,n51,60)
graph.add_edge(e4251)
e5161 = Edge(n51,n61,72)
graph.add_edge(e5161)
e6162 = Edge(n61,n62,60)
graph.add_edge(e6162)
e5262 = Edge(n52,n62,90)
graph.add_edge(e5262)
e5253 = Edge(n52,n53,120)
graph.add_edge(e5253)
e4243 = Edge(n42,n43,135)
graph.add_edge(e4243)
e3342 = Edge(n33,n42,135)
graph.add_edge(e3342)
e4353 = Edge(n43,n53,135)
graph.add_edge(e4353)
e1323 = Edge(n13,n23,36)
graph.add_edge(e1323)
e2333 = Edge(n23,n33,120)
graph.add_edge(e2333)
e3343 = Edge(n33,n43,180)
graph.add_edge(e3343)
e2324 = Edge(n23,n24,120)
graph.add_edge(e2324)
e2334 = Edge(n23,n34,180)
graph.add_edge(e2334)
e3343 = Edge(n33,n43,240)
graph.add_edge(e3343)
e3334 = Edge(n33,n34,120)
graph.add_edge(e3334)
e4344 = Edge(n43,n44,90)
graph.add_edge(e4344)
e4453 = Edge(n44,n53,240)
graph.add_edge(e4453)
e2434 = Edge(n24,n34,120)
graph.add_edge(e2434)
e3444 = Edge(n34,n44,180)
graph.add_edge(e3444)
e4454 = Edge(n44,n54,135)
graph.add_edge(e4454)
e2425 = Edge(n24,n25,195)
graph.add_edge(e2425)
e3435 = Edge(n34,n35,120)
graph.add_edge(e3435)
e3445 = Edge(n34,n45,240)
graph.add_edge(e3445)
e4435 = Edge(n44,n35,240)
graph.add_edge(e4435)
e4445 = Edge(n44,n45,135)
graph.add_edge(e4445)
e2535 = Edge(n25,n35,120)
graph.add_edge(e2535)
e3545 = Edge(n35,n45,210)
graph.add_edge(e3545)
e4555 = Edge(n45,n55,120)
graph.add_edge(e4555)
e2526 = Edge(n25,n26,135)
graph.add_edge(e2526)
e3536 = Edge(n35,n36,150)
graph.add_edge(e3536)
e3546 = Edge(n35,n46,240)
graph.add_edge(e3546)
e3645 = Edge(n36,n45,150)
graph.add_edge(e3645)
e4546 = Edge(n45,n46,120)
graph.add_edge(e4546)
e4556 = Edge(n45,n56,180)
graph.add_edge(e4556)
