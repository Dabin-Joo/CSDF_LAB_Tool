import json
import pandas as pd
import os
import csv
def json_analyze(jsonfile):
    with open(jsonfile,'r',encoding='utf-8') as f:
        info=json.load(f)
        
        #print(type(info.keys()))
        #print(info['teamId'])
    #info = json.loads(jsonfile)
        try:
            if 'records' not in info:
                
                contents=[info['teamId'], info['writerId'], info['updatedAt']]
                if 'body' in info['content']:
                    contents.append(info['content']['body'])
                else:
                    contents.append(info['content']['title'])
                print(contents)
                
                    
            if 'records' in info:
                if len(info['records'])!=0:
                    for i in (0,len(info['records'])-1):
                        contents=[info['records'][i]['message']['teamId'],info['records'][i]['message']['writerId'],info['records'][i]['message']['updatedAt'],
                                info['records'][i]['message']['content']]
                else:
                    contents=[]
           
        except KeyError:
            try: 
                if len(info['comments'])!=0:
                    contents=[info['comments'][0]['teamId'], info['comments'][0]['writerId'], info['comments'][0]['updatedAt']]
                    if 'body' in info['comments'][0]['content']:
                        contents.append(info['comments'][0]['content']['body'])
                    else:
                        contents.append(info['comments'][0]['content']['title'])
                else:
                    contents=[]
            except KeyError:
                #투표 기록/ 추후 수정 필요
                if 'poll' in info:
                    contents=[]
                else: contents=[info['records'][0]['teamId'],info['records'][0]['id'],'Chat created']
                
        except AttributeError:
            contents=[info[0]['teamId'], info[0]['writerId'], info[0]['updatedAt']]
            if 'body' in info[0]:
                contents.append(info[0]['content']['body'])
            else:
                contents.append(info[0]['content']['title'])
        except TypeError:
            for i in (0,len(info)-1):
                contents=[info[0]['teamId'], info[0]['writerId'], info[0]['updatedAt']]
            if 'body' in info[0]:
                contents.append(info[0]['content']['body'])
            else:
                contents.append(info[0]['content']['title'])
            
            with open('output.csv','a',newline='') as f:
                write=csv.writer(f)
                write.writerow(contents)
                
    if os.path.exists('output.csv'):
        with open('output.csv','a',newline='') as f:
            write=csv.writer(f)
            write.writerow(contents)
            
        #contents.to_csv('output.csv', index=False, mode='w', encoding='utf-8-sig')
    # else:
    #     with open('output.csv','a',newline='') as f:
    #         write=csv.writer(f)
    #         write.writerow(contents)
        #contents.to_csv('output.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    
        # record=json_data['record']
    # for i in record:
    #     record[i]=json_data+i
    #     try: content=(json_data+i)['message']['content']['body']
    #     except ValueError:
    #         content=(json_data+i)['feedback']['content']['body']