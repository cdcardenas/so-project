from subprocess import Popen, PIPE

def get_all_stats():
  grep_process = Popen(["vmstat", "-s","-S","m"], stdout=PIPE,stderr=PIPE)
  listado_stats= Popen(["awk", '-F', ':','{print $1}' ],stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  
  print(listado_stats)
  return filter(None, listado_stats)


def get_hdd():
  grep_process = Popen(["df", "/dev/sda1", "-h"], stdout=PIPE, stderr=PIPE)
  lista= Popen(["awk",'{print $4}' ],stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n') 
  return filter(None, lista)

def get_cpu():
  grep_process = Popen(["sar", "1", "1"], stdout=PIPE, stderr=PIPE)
  lista = Popen(["awk", '{print $5}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None, lista)

def get_service():
  grep_process = Popen(["service", "sshd", "status"], stdout=PIPE, stderr=PIPE)
  lista = Popen(["awk", '-F', 'Active:', '{print $2}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')

  return filter(None, lista)




