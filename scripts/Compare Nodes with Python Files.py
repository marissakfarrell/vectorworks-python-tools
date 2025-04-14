import os
import re

# Step 1: Get all Python files and extract defined node names
folder_path = vs.GetFolderPath(191)
node_file_map = []

pattern = re.compile(r'this\s*=\s*Marionette\.Node\s*\(\s*["\'](.+?)["\']\s*\)')

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                match = pattern.search(content)
                if match:
                    node_name = match.group(1)
                    node_file_map.append((file, node_name))
            except:
                pass

# Step 2: Get actual node names in the current document using MarionetteNode record
resource_node_names = []
list_id, count = vs.BuildResourceList(16, 1, '', False)

for i in range(1, count + 1):
    res_name = vs.GetNameFromResourceList(list_id, i)
    wrapper_handle = vs.GetObject(res_name)
    if wrapper_handle:
        node_handle = vs.FInGroup(wrapper_handle)
        if node_handle:
            node_name = vs.GetRField(node_handle, 'MarionetteNode', 'NodeType')
            if node_name:
                resource_node_names.append(node_name)
vs.AlrtDialog(str(resource_node_names))
# Step 3: Compare
missing_files = []
for file_name, node_name in node_file_map:
    if node_name not in resource_node_names:
        missing_files.append(file_name)

# Step 4: Output
if missing_files:
    vs.AlrtDialog("Files Missing Matching Node Resource", "\n".join(missing_files))
else:
    vs.AlrtDialog("All node scripts have matching node resources.")
    
vs.AlrtDialog(str(len(missing_files)) + ' ' + str(len(resource_node_names)) + ' ' + str(len(node_file_map)))
