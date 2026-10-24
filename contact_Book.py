from pathlib import Path
import json 

class contact :
    database = 'contact.json'
    data=[]
    try:
        if Path(database).exists(): 
            with open(database)as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an execption occured as {err}")
    @classmethod
    def __update(cls):
        with open (cls.database,'w')as fs:
            fs.write(json.dumps(contact.data))
    def add(self):
        a={
            "name":input("enter the name "),
            "number":int(input("enter the number ")),
            "email":input("enter the email "),
            "address":input("enter the address ")
        }
        contact.data.append(a)
        contact.__update()
        print("add contact successfully")
        print(a)
    def view(self):
        v=contact.data
        try:
            for j in v:
                print(j)
                print("------------")
        except Exception as err:
            print(f"an execption occured as {err}")

    def search(self):
        name=input("Please tell me to search the name :- ")
        v=contact.data
        o=[j for j in v if j["name"]==name]
        if o :
            print(o)
        else:
            print("not found")
    def edit(self):
        name=input("Please tell me to search the name :- ")
        v=contact.data
        o=[j for j in v if j["name"]==name]
        if o :
            userdata=[i for i in contact.data if i['name']==name ]
            print(userdata)
            print("You not change the name ,email , address to enter press ")
            newdata={
                "name":input("update the name  "),
                "email":input("update the email "),
                "address":input("update the address ")
                }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']
            if newdata["address"]=="":
                newdata["address"]=userdata[0]['address']  
            n=input("You change the number enter the number :- 1 ")
            if n=="1":
                newdata={
                    "number":input("update the number ")
                }
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
            contact.__update()
            print("add contact successfully")
            print(newdata)
        else:
            print("not found")

    def delete(self):
        name=input("Please tell me to search the name :- ")
        v=contact.data
        o=[j for j in v if j["name"]==name]
        if o:
            index=contact.data.index(o[0])
            contact.data.pop(index)
            print("contact deleted succefully ")
            contact.__update()
        else:
            print("not found")


                
user=contact()
print("--Contact Book--")
print("1.Add Contact")
print("2.View Contact")
print("3.Search Contact")
print("4.Edit Contact")
print("5.Delete Contact")
a=int(input("Enter the number to used this "))
if a==1:
    user.add()
if a==2:
    user.view()
if a==3:
    user.search()
if a==4:
    user.edit()
if a==5:
    user.delete()