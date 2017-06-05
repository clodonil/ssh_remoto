# -*- coding: utf-8 -*-
import paramiko
import datetime

#################################################

class Remoto_ssh:
   def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.acesso = {}

   def conexao(self, ip, porta,login,senha):
        self.acesso['login']=login
        self.acesso['senha']=senha
        try:
            self.ssh.connect(ip, port=porta, username=self.acesso['login'], password=self.acesso['senha'])
            return True
        except:
           return False


   def execute(self,command,sudo="no"):
       retorno=[]
       flag=0



       if sudo == "sudo":
           #command = "echo '{0}' | sudo -S {1}".format(self.acesso['senha'],command)
           command = "sudo -S {0}".format(command)
           stdin, stdout, stderr = self.ssh.exec_command(command)
           stdin.write("#")
           stdin.flush()
       else:
           stdin, stdout, stderr = self.ssh.exec_command(command)

       if stdout.channel.recv_exit_status() != 0:
          retorno.append(stderr.readlines())
          flag=1
       else:
           retorno.append(stdout.readlines())


       if flag:
          retorno.append("ERROR")
       else:
          retorno.append('OK')
       return(retorno)

   def close(self):
       self.ssh.close()

