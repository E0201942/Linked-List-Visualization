import tkinter
selectedNode = None
window = tkinter.Tk()
objective = tkinter.Tk()
objective.title("Objectives")
window.title("GUI")
actions = ""
variableList = {"head" : None, "node": None, "store1":None, "store2": None}
correctNode = None
node = None
nodeVal = tkinter.StringVar()
nodeNext = tkinter.StringVar()
remarks = tkinter.StringVar()
def checkObjective1():
    global variableList
    count = 0
    node = variableList["head"]
    if node != None:
        while node.next!= None:
            count+=1
            node = node.next
    count +=1
    return (count == 9)
def checkObjective2():
    global variableList
    if variableList["node"].next != None and variableList["node"].next.next == None:
        return True
    return False
def checkObjective3():
    global variableList
    if variableList["node"].next == None:
        return True
    return False
def checkObjective4():
    global variableList
    node = variableList["node"]
    if node.next == None:
        return False
    if node.next.next == None:
        return False
    if node.next.next.next == None:
        return False
    if node.next.next.next.next == None:
        return True
    else:
        return False
def checkObjective5():
    global variableList
    node = variableList["node"]
    if node.next == None:
        return False
    if node.next.next == None:
        return True
    return False
def updateNodes():
    global window
    global variableList
    node = variableList["head"]
    i =0
    storeChecked1 = False
    storeChecked2 = False
    nodeChecked = False
    if node!= None:
        while node.next != None:
            if node == variableList["node"] and node == variableList["head"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "white", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked1 = True
            elif node == variableList["node"] and node == variableList["head"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "white", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked2 = True
            elif node == variableList["node"] and node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "purple", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
            elif node == variableList["head"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "orange", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
            elif node == variableList["node"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked1 = True
            elif node == variableList["head"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "orange", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
            elif node == variableList["node"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked2 = True
            elif node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
            elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
            elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
            elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
            else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
            i+=1
            w= tkinter.Label(window, text = str("->")).grid(row = 0, column = i)
            i+=1
            node = node.next
        
        if node == variableList["node"] and node == variableList["head"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "white", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked1 = True
        elif node == variableList["node"] and node == variableList["head"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "white", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked2 = True
        elif node == variableList["node"] and node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "purple", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
        elif node == variableList["head"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "orange", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
        elif node == variableList["node"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked1 = True
        elif node == variableList["head"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "orange", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
        elif node == variableList["node"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
                storeChecked2 = True
        elif node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
        elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
        elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
        elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
        else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
        i+=1
    if storeChecked1 == False and variableList["store1"]!= None:
        start = i
        node = variableList["store1"]
        while node.next != None:
            if node.next == variableList["head"]:
                 for label in window.grid_slaves():
                     if int(label.grid_info()["column"]) < start and int(label.grid_info()["row"] == 0):
                         label.grid_forget()
                         node = variableList["store1"]
                         i = 0
                
            if node == variableList["node"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
            elif node == variableList["store2"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
            elif node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
            elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
            elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
            elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
            else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
            i+=1
            w= tkinter.Label(window, text = str("->")).grid(row = 0, column = i)
            i+=1
            node = node.next
    
        if node == variableList["node"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                nodeChecked = True
        elif node == variableList["store2"] and node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
        elif node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
        elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
        elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
        elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
        else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
        
        i+=1
    if nodeChecked == False and variableList["node"] != None:
        start = i
        node = variableList["node"]
        while node.next != None:
            if node.next == variableList["head"] or node.next == variableList["store1"]:
                 for label in window.grid_slaves():
                     if int(label.grid_info()["column"]) < start and int(label.grid_info()["row"] == 0):
                         label.grid_forget()
                         node = variableList["node"]
                         i = 0
            if node == variableList["node"] and node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
                
            elif node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
            elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
            elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
            elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
            
            else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
            i+=1
            w= tkinter.Label(window, text = str("->")).grid(row = 0, column = i)
            i+=1
            node = node.next
    
        if node == variableList["node"] and node == variableList["store2"]:
            w= tkinter.Label(window, text = str(node.val), bg = "green", fg = "black").grid(row = 0, column = i)
            storeChecked2 = True
                
        elif node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
        elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
        elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
        elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
        else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
        i+=1
    if storeChecked2 == False and variableList["store2"]!= None:
        start = i
        node = variableList["store2"]
        while node.next!= None:
            print("here")
            if node.next == variableList["head"] or node.next == variableList["store1"] or node.next == variableList["node"]:
                 for label in window.grid_slaves():
                     if int(label.grid_info()["column"]) < start and int(label.grid_info()["row"] == 0):
                         label.grid_forget()
                         node = variableList["store2"]
                         i = 0
            
            if node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                nodeChecked = True
            elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
            elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                storeChecked1 = True
            elif node == variableList["store2"]:
                w= tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
                storeChecked2 = True
            else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
            i+=1
            w= tkinter.Label(window, text = str("->")).grid(row = 0, column = i)
            i+=1
            node = node.next
       
        if node == variableList["node"]:
                w= tkinter.Label(window, text = str(node.val), bg = "blue", fg = "white").grid(row = 0, column = i)
                
        elif node == variableList["head"]:
                w= tkinter.Label(window, text = str(node.val), bg = "red", fg = "black").grid(row = 0, column = i)
                
        elif node == variableList["store1"]:
                w= tkinter.Label(window, text = str(node.val), bg = "yellow", fg = "black").grid(row = 0, column = i)
                
        elif node == variableList["store2"]:
                tkinter.Label(window, text = str(node.val), bg = "pink", fg = "black").grid(row = 0, column = i)
        else:
                w= tkinter.Label(window, text = str(node.val), bg = "grey", fg = "black").grid(row = 0, column = i)
                
        i+=1
        
    for label in window.grid_slaves():
        if int(label.grid_info()["column"]) >= i and int(label.grid_info()["row"] == 0):
            label.grid_forget()
def goStart(target):
    global variableList
    global actions
    variableList[target] = variableList["head"]
    actions+= target+" = head\n"
    updateNodes()
    updateActions()
def goStore1(target):
    global variableList
    global actions
    variableList[target] = variableList["store1"]
    actions += target+ " = store1\n"
    updateNodes()
    updateActions()
def goStore2(target):
    global variableList
    global actions
    variableList[target] = variableList["store2"]
    actions += target+ " = store2\n"
    updateNodes()
    updateActions()
def goNode(target):
    global variableList
    global actions
    global objective
    variableList[target] = variableList["node"]
    actions += target+ " = node\n"
    if checkObjective1():
        tkinter.Label(objective, text = "Create a linked list with 9 nodes", fg = "green" ).grid(row =0, column = 0, columnspan = 10)
    updateNodes()
    updateActions()
def goNextNode(target):
    global variableList
    global actions
    variableList[target] = variableList["node"].next
    actions += target+ " = node.next\n"
    updateNodes()
    updateActions()
def addRemark():
    global actions
    global remark
    rem = remark.get()
    actions += remark +"\n"
def createNode():
    global nodeVal
    global variableList
    global actions
    global nodeNext
    global correctNode
    val = nodeVal.get()
    nextn = nodeNext.get()
    if nextn in variableList.keys():
        node = Node(str(val))
        node.next = variableList[nextn]
        actions += "node = Node(" + val + ", " + nextn + ")\n"
        variableList["node"] = node
        if checkObjective5():
            correctNode = node
        updateNodes()
        updateActions()
    elif nextn == "None":
        node = Node(str(val))
        actions += "node = Node(" + val + ", None)\n"
        variableList["node"] = node
        updateNodes()
        updateActions()
   
        
def updateNextNode(target):
    global variableList
    global actions
    if target != None:
        if checkObjective3():
            tkinter.Label(objective, text = "Insert a node at the end of the list", fg = "green" ).grid(row =2, column = 0, columnspan = 10)
        if checkObjective4():
            tkinter.Label(objective, text = "Delete the 3rd last node", fg = "green" ).grid(row =3, column = 0, columnspan = 10)
        variableList["node"].next = variableList[target]
        if variableList[target] == correctNode:
            tkinter.Label(objective, text = "Insert a node at the 2nd last position in the list", fg = "green" ).grid(row =4, column = 0, columnspan = 10)
        actions+= "node.next = " + target +"\n"
    else:
        if checkObjective2():
            tkinter.Label(objective, text = "Delete the last node", fg = "green" ).grid(row =1, column = 0, columnspan = 10)
        variableList["node"].next = None
        actions+= "node.next = None\n"
        
    updateActions()
    updateNodes()
def reset():
    global variableList
    global actions
    global window
    for label in window.grid_slaves():
        if int(label.grid_info()["row"]) == 0 or int(label.grid_info()["row"] == 8):
            label.grid_forget()

    for x in variableList:
        variableList[x] = None
    actions = ""
    updateActions
    updateNodes()
def updateActions():
    w= tkinter.Label(window, text = str(actions)).grid(row = 8, columnspan = 8)
        
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing
    def traverse(self):
        global actions
        node = self # start from the head node
        if self.next != None:
            variableList["node"] = self.next
        updateNodes()
        actions += "node = node.next\n"
        updateActions()
    def display(self):
        print(self.val)
    def updatePointer(self, newPointer):
        self.pointer = newPointer
    def updateValue(self, value):
        self.val = value

#node = Node(  ,  )
btn4 = tkinter.Label(window, text = "node =",fg="white", bg = "blue").grid(row =1, column = 0, columnspan = 3)
tkinter.Label(window, text = "(", fg = "black").grid(row =1, column = 6)
tkinter.Entry(window,textvariable=nodeVal,width = 6).grid(row = 1, column = 6, columnspan = 5)
tkinter.Label(window, text = ",", fg = "black").grid(row =1, column = 10)
tkinter.Entry(window,textvariable=nodeNext, width = 10).grid(row = 1, column = 11, columnspan = 5)
tkinter.Button(window, text = "Node", fg = "black", command = lambda: createNode()).grid(row = 1, column = 3, columnspan = 3)
tkinter.Label(window, text = ")", fg = "black").grid(row =1, column = 17)
#node =
tkinter.Label(window, text = "node =", fg="white", bg = "blue").grid(row =2, column = 0, columnspan = 3)
tkinter.Button(window, text = "node.next", fg = "black", command = lambda: variableList["node"].traverse()).grid(row = 2, column = 3, columnspan = 5)
tkinter.Button(window, text = "head", fg="white", bg = "red", command = lambda: goStart("node")).grid(row = 2, column = 8, columnspan = 2)
tkinter.Button(window, text = "store1", bg = "yellow", fg= "black", command = lambda: goStore1("node")).grid(row = 2, column = 10, columnspan = 3)
tkinter.Button(window, text = "store2", fg = "black", bg= "pink", command = lambda: goStore2("node")).grid(row = 2, column = 12, columnspan = 3)
#store1 =
tkinter.Label(window, text = "store1 =", bg = "yellow", fg= "black").grid(row =3, column = 0, columnspan = 3)
tkinter.Button(window, text = "node.next", fg = "black", command = lambda: goNextNode("store1")).grid(row = 3, column = 3, columnspan = 5)
tkinter.Button(window, text = "head", fg="white", bg = "red", command = lambda: goStart("store1")).grid(row = 3, column = 8, columnspan = 2)
tkinter.Button(window, text = "node", fg="white", bg = "blue", command = lambda: goNode("store1")).grid(row = 3, column = 10, columnspan = 3)
tkinter.Button(window, text = "store2", fg = "black", bg= "pink", command = lambda: goStore2("store1")).grid(row = 3, column = 12, columnspan = 3)
#store2 =
tkinter.Label(window, text = "store2 =", fg = "black", bg= "pink").grid(row =4, column = 0, columnspan = 3)
tkinter.Button(window, text = "node.next", fg = "black", command = lambda: goNextNode("store2")).grid(row = 4, column = 3, columnspan = 5)
tkinter.Button(window, text = "head",fg="white", bg = "red", command = lambda: goStart("store2")).grid(row = 4, column = 8, columnspan = 2)
tkinter.Button(window, text = "node", fg="white", bg = "blue", command = lambda: goNode("store2")).grid(row = 4, column = 10, columnspan = 3)
tkinter.Button(window, text = "store1",  bg = "yellow", fg= "black", command = lambda: goStore1("store2")).grid(row = 4, column = 12, columnspan = 3)
#head =
tkinter.Label(window, text = "head =", fg="white", bg = "red" ).grid(row =5, column = 0, columnspan = 3)
tkinter.Button(window, text = "node.next", fg = "black", command = lambda: goNextNode("head")).grid(row = 5, column = 3, columnspan = 5)
tkinter.Button(window, text = "node", fg="white", bg = "blue", command = lambda: goNode("head")).grid(row = 5, column = 7, columnspan = 3)
tkinter.Button(window, text = "store2", fg = "black", bg= "pink", command = lambda: goStore2("head")).grid(row = 5, column = 12, columnspan = 3)
tkinter.Button(window, text = "store1", bg = "yellow", fg= "black", command = lambda: goStore1("head")).grid(row = 5, column = 10, columnspan = 3)

#node.next =
tkinter.Label(window, text = "node.next =", fg = "black" ).grid(row =6, column = 0, columnspan = 5)
tkinter.Button(window, text = "head", fg="white", bg = "red", command = lambda: updateNextNode("head")).grid(row = 6, column = 7, columnspan = 3)
tkinter.Button(window, text = "node", fg="white", bg = "blue", command = lambda: updateNextNode("node")).grid(row = 6, column = 10, columnspan = 3)
tkinter.Button(window, text = "store2", fg = "black", bg= "pink", command = lambda: updateNextNode("store2")).grid(row = 6, column = 15, columnspan = 3)
tkinter.Button(window, text = "store1", bg = "yellow", fg= "black", command = lambda: updateNextNode("store1")).grid(row = 6, column = 12, columnspan = 3)
tkinter.Button(window, text = "None", bg = "black", fg= "white", command = lambda: updateNextNode(None)).grid(row = 6, column =5, columnspan = 2)
#reset and remarks
tkinter.Button(window, text = "Reset", fg = "black", bg = "red", command = lambda: reset()).grid(row = 7, column = 0, columnspan = 3)
tkinter.Entry(window,textvariable=remarks,width = 21).grid(row = 7, column = 3, columnspan = 10)
tkinter.Button(window, text = "Add Remark", fg = "white", bg = "green", command = lambda: addRemark()).grid(row = 7, column = 13, columnspan = 3)
#objectives
tkinter.Label(objective, text = "Create a linked list with 9 nodes", fg = "red" ).grid(row =0, column = 0, columnspan = 10)
tkinter.Label(objective, text = "Delete the last node", fg = "red" ).grid(row =1, column = 0, columnspan = 10)
tkinter.Label(objective, text = "Insert a node at the end of the list", fg = "red" ).grid(row =2, column = 0, columnspan = 10)
tkinter.Label(objective, text = "Delete the 3rd last node", fg = "red" ).grid(row =3, column = 0, columnspan = 10)
tkinter.Label(objective, text = "Insert a node at the 2nd last position in the list", fg = "red" ).grid(row =4, column = 0, columnspan = 10)
window.mainloop()
