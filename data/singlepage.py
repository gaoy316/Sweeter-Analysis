import urllib
import urllib2
import re
import pandas as pd

def single_page(i):
    url = 'http://bioinf-applied.charite.de/sweet/index.php?site=detail_view&ids=('+str(i)+')&path='
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    pageCode = response.read().decode('cp1252')
    items = list()
    
    pattern = re.compile('<tr><td> Name </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Class </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> SMILES </td><td><.*?value="(.*?)"></td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('SMILES.*?<tr><td> Class </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Calories </td><td>ADI: (.*?)mg/kg</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
    
    pattern = re.compile('<tr><td> Sweetness </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile( '<tr><td> Origin </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile( '<tr><td> Approval </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Therapeutic effect </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Metabolism </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Therapeutic annotation </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Formula </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Molweight </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Atoms </td><td>(.*?)</td></tr><tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Heavy Atoms </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Rings </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> Bonds </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile( '<tr><td> Rotatable Bonds </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> H-bond Donors </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    pattern = re.compile('<tr><td> H-bond Acceptors </td><td>(.*?)</td></tr>',re.S)
    item = re.findall(pattern,pageCode)
    if item:
        items.append(item[0])
    else:
        item = None
        items.append(item)
        
    df = pd.DataFrame(items)
    df1 = df.transpose
    
    return df1