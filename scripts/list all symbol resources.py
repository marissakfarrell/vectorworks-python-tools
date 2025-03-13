'''
this script will list all symbol resources and their parent folder and output
to a text file with the same name as the file in the user folder
'''
import os

resID = 16
pathID = 113

MyList, cnt = vs.BuildResourceList2(resID, 0, '', False)
MyName = vs.GetNameFromResourceList(MyList, 1)
syms = []
i = 1
while i < cnt+5:
	syms.append((vs.GetNameFromResourceList(MyList, i),vs.GetName(vs.GetParent(vs.GetObject(vs.GetNameFromResourceList(MyList, i))))))
	i += 1

fPath = vs.GetFolderPath(12)

parents = []
for sym in syms:
	parents.append(str(vs.GetName(vs.GetParent(vs.GetObject(sym[0])))))

file_name = vs.GetFName().split(".")[0]+".txt"
file_path = os.path.join(fPath, file_name)

try:
	if not os.path.exists(fPath):
		os.makedirs(fPath)
	with open(file_path, 'w') as file:
		for sym in syms:
			file.write(sym[0] + ", " + sym[1] + '\n')
	print(f"File '{file_path}' created successfully.")
except Exception as e:
	print(f"An error occurred: {e}")