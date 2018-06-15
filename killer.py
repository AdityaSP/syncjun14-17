import subprocess
output = subprocess.check_output('tasklist')
#print output[:1000]

lines = output.split("\r\n")
#print len(lines[3:])

def getlines(line):
    return 'chrome' in line
    
chrome_lines = filter(getlines, lines)
#print len(chrome_lines)
#print chrome_lines[:3]

#['chrome.exe                    5460 Console                    1    200,352 K', 'chrome.exe                    1272 Console                    1      5,728 K', 'chrome.exe                    3880 Console                    1      6,088 K']

chrome_split = [ line.split() for line in chrome_lines]

#print chrome_split[:3]
#[
#    ['chrome.exe', '5460', 'Console', '1', '200,396', 'K'], 
#    ['chrome.exe', '1272', 'Console', '1', '5,728', 'K'], 
#    ['chrome.exe', '3880', 'Console', '1', '6,088', 'K']
#]

pids = [ item[1] for item in chrome_split]

#['5460', '1272', '3880', '6908', '936', '376', '2316', '2656', '4912', '3220', '5200','2860', '4952', '6024', '7144', '11060', '7164', '10140', '9164', '4684', '9924']

print pids

for pid in pids:
    subprocess.call('taskkill /f /pid ' + pid)
    
    
