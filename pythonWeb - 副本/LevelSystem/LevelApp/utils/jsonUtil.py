import json

from django.conf import settings


# 读取JSON文件
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# 写入JSON文件
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


# 增加数据
def add_data_json(data, atlas_type, new_data):
    atlas = data.get(atlas_type, [])
    atlas.append(new_data)
    data[atlas_type] = atlas
    # 写入JSON文件
    write_json_file(settings.JSON_FILE_PATH, data)
    return True


# 删除数据
def delete_data(data, atlas_type, id_to_delete):
    atlas = data.get(atlas_type, [])
    data[atlas_type] = [item for item in atlas if item['id'] != int(id_to_delete)]
    print(data[atlas_type])
    # 写入JSON文件
    write_json_file(settings.JSON_FILE_PATH, data)
    return True


# 修改数据
def update_data(data, atlas_type, updated_data):
    atlas = data.get(atlas_type, [])
    for item in atlas:
        if item['id'] == updated_data['id']:
            item.update(updated_data)
            # 写入JSON文件
            write_json_file(settings.JSON_FILE_PATH, data)
            return True
    return False


# 查询数据
def query_data(data, atlas_type, id_to_query):
    atlas = data.get(atlas_type, [])
    for item in atlas:
        if item['id'] == id_to_query:
            return item
    return None


# 查询所有atlas_type 类型中的所有数据
def query_all_issue_data(data, atlas_type):
    return data.get(atlas_type, [])

