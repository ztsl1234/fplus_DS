#implement pythnpkg
#reconcil
#2 data source and sink dataset
#trn data - each 4 fields - instrument id, trn date, qty, price
#return only trn found in source dataset but not the sink dataset
#return only trn found in sink matching but not in source dataset
#return trn in both source and sink

def return_all(data1, data2):
    return (data1+data2)

def diff(data1, data2):

    data1_only=[]
    for data1_record in data1:
        found=False
        for data2_record in data2:
            if data1_record == data2_record:
                found=True
        if not found:
            data1_only.append(data1_record)
    
    print(data1_only)
   
    return data1_only








