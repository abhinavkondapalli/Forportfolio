#!/usr/bin/env python
# coding: utf-8

# In[11]:


print('Select your Bachelors Degree:\n 1: Bachelor of Commerce \n 2: BAchelor of IT \n 3: Others')
b_degree = input()
b_degree = int(b_degree)


# In[12]:


print('Country of Bachelor Degree')
country = input()
if not country == "Australia":
    print("Please enter your IELTS Score")
    ielts = input()
    ielts = float(ielts)
print('Years of Experience after your Bachelors')
exp_after_b = int(input())
   


# In[13]:


print('Masters Degree:\n 1: Currently in University(3rd Sem) \n 2: Currently in University(4th Sem) \n 3: Completed Masters Degree')
m_deg_completion = int(input())
if(m_deg_completion == 3):
    print('Years of Experience after your Masters Degree')
    exp_after_m = int(input())


# In[17]:



#No experience after Masters
print('Select your Masters Degree:\n 1.Business Analytics\n 2:Masters in IT\n 3:Masters in Data Sc\n 4:Masters in Computer Sc.')
m_degree = input()
m_degree = int(m_degree)

print("Select top skills:\n 1:Power BI or Tableau \n 2:StakeHolder \n 3:Agile Methodologies \n 4:Python \n 5: SQL \n 6: Any other Programming Language \n 7: Azure or AWS \n 8: Exit")
i =0
skill = []
while (True):
    p=input()
    p = int(p)
    if(p>0 and p<8):
        skill.insert(i,p)
        i+=1
    if(p==8):
        print("Thank You")
        break

if(m_degree == 1 and len(skill) == 1 and 1 in skill) == True:
    print("BI & Reporting")
    
elif(m_degree == 1 and len(skill) == 2 and 4 in skill and 5 in skill) == True:
    print("Data Analyst")
    
elif(m_degree == 2 and len(skill) == 2 and 2 in skill and 3 in skill) == True:
    print("Business Analyst")

elif(m_degree == 3 and len(skill) == 2 and 4 in skill and 5 in skill) == True:
    print("Data Analyst")

elif(m_degree == 4 and len(skill) == 1 and 6 in skill) == True:
    print("Software Developer")

elif(m_degree == 4 and len(skill) == 1 and 7 in skill) == True:
    print("DevOps or Cloud Engineer")
else:
    print("No roles available")


# In[ ]:





# ##### 

# In[10]:


#Experience after Masters
if(exp_after_m > 0):
    print("Select the role you want to work")
    print("1.BI & Reporting \n 2.Business Analyst \n 3.Data Analyst \n 4. Software Developer \n 5. DevOps/Cloud Engineer")
    role = int(input())
    print("Enter experience in each technology")
    t_exp = 1
    if(role == 1):
        print("PowerBI")
        e1 = int(input())
        print("Tableau")
        e2 = int(input())
        t_exp = e1 * e2
    if(role == 2):
        print("StakeHolder")
        e1 = int(input())
        print("Agile")
        e2 = int(input())
        t_exp = e1 * e2
    if(role == 3):
        print("Python")
        e1 = int(input())
        print("SQL")
        e2 = int(input())
        t_exp = e1 * e2
    if(role == 4):
        print("Programming Language")
        e1 = int(input())
        t_exp = e1
    if(role == 5):
        print("AWS/Azure")
        e1 = int(input())
        t_exp = e1

if(t_exp == 0):
    print("Role not suitable")
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




