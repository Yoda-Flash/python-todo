m_toDo = ["To Do:"]

def getLength():
    len(m_toDo)

def addItem(item):
    m_toDo.append(item)

def deleteItemByIndex(index):
    m_toDo.pop(index)

def deleteItemByName(item):
    m_toDo.remove(item)

addItem("Play")
addItem("program")
addItem("code")

for x in m_toDo:    
    print(x)

deleteItemByIndex(3)
deleteItemByName("program")