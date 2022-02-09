def read_text_file_column_1(file_name): 
    f=open(file_name+'.txt','r')
    lines=f.readlines()
    all_sku=[]
    for i in lines:
        i=i.replace('\n','')
        all_sku.append(i)
    return all_sku

list1={}
count=0
tap=0
pop=1
data_1="data"
file=read_text_file_column_1(data_1)
for i in file:
	list1[count]=i
	count+=1
print(list1)

with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    fieldnames=["a","b"]
    writer.writerows()
    for i in range(1,200):
    	writer.writerows({'a' : list1[tap], 'b' : list1[pop]})
    	pop+=2
    	tap+=2	

