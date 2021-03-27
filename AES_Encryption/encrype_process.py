from AES_Encryption.en_decrype import *
import json
import os
'''
用法:僅須在程式中使用:
conn,cursor = check_encrype('Any_string_you_define')
'''
def input_new_encrype(fuc_name):
    print(f'Starting input ......{fuc_name}')
    user_id = input('Please input gmail address:')
    password = input('Please input password:')

    key_path,result_path = read_control()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    key = get_key()
    user_encrype = aes_encrypt(user_id, key)
    password_encrype = aes_encrypt(password, key)
    store_encrype = dict()
    store_encrype['name'] = fuc_name
    store_encrype['user_id'] = user_encrype
    store_encrype['password'] = password_encrype
    with open(result_path, 'a') as outfile:
        json.dump(store_encrype, outfile)
        outfile.write('\n')
    outfile.close()
    print('Encrype Over !')
    exit()
    return None

def check_encrype(eng_name):
    status = 0
    key_path,result_path = read_control()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    if os.path.isfile(result_path):
        pass
    else:      
        open(result_path,"a")
    with open(result_path,'r') as json_file:
        each_line = json_file.readlines()
        json_file.close()
        if len(each_line)!=0:
            for line in each_line:
                json_line = json.loads(line)
                if json_line['name'] ==eng_name:  
                    status+=1
                    key = get_key()
                    user_id = aes_decrypt(json_line['user_id'],key)
                    password = aes_decrypt(json_line['password'],key)
            if status ==0:
                input_new_encrype(eng_name)              
        else:
            input_new_encrype(eng_name)
    return user_id,password
