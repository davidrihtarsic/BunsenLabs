#!/usr/bin/python3

from shellTUI import Form, Edit, Text, cls, setCursor
import sys
import os

cls()

user_path = os.path.expanduser('~')
user = user_path[user_path.rfind("/")+1:]
download_dir = user_path + '/Downloads/'
opt_dir = '/opt/'
menu_desktop = '/usr/share/applications/'
profile_dir = '/etc/profile.d/'
escapeColorDefault = '\x1B[39m'
escapeColorCmd = '\x1B[38;5;130m'
escapeColorInstalled = '\x1B[32m'
thisAppOutput = escapeColorCmd+'--> '
confirmText = escapeColorDefault+' [y/n]:'
vsi_programi = []

def deBug(info):
    print(info)
    input()

## CLASS NovProgram #######################################

class NovProgram(object):
    def __init__(self):
        super(NovProgram, self).__init__()
        self.program_name = ''
        self.index = 0
        self.category = ''
        self.description = ''
        self.notes = ''
        # instalation variables---------------
        self.shell_pre_install_cmds = []
        self.apt_get_install_cmds = []
        self.deb_package_path = ''
        self.deb_package_file = ''
        self.deb_package_path_32 = ''
        self.deb_package_file_32 = ''
        self.deb_package_path_64 = ''
        self.deb_package_file_64 = ''
# tar installation variables - - - - - - - - 
        self.tar_package_path = ''
        self.tar_package_file = ''
        self.tar_package_path_32 = ''
        self.tar_package_file_32 = ''
        self.tar_package_path_64 = ''
        self.tar_package_file_64 = ''
        self.tar_destination = '' # default je /opt/IME_PROGRAMA
        self.tar_extra_cmds = []
# shell post install - - - - - - - - - - - - 
        self.shell_post_install_cmds = []
        self.check_version_cmd = ''
        self.auto_install = False

        self.arhitecture_64bit = False
        self.arhitecture_32bit = False
        self.arhitecture_bit_num = 0
        if sys.maxsize > 2**32 :
            self.arhitecture_64bit = True
            self.arhitecture_bit_num = 64
        else:
            self.arhitecture_32bit = True
            self.arhitecture_bit_num = 32

    def apt_get_install(self):
        # install from terminal command
        if len(self.apt_get_install_cmds) != 0:
            for apt_cmd in self.apt_get_install_cmds:
                if self.auto_install:
                    if self.version_check():
                        # it is alredy installed... skip it!
                        pass
                    else:
                        # it is not installed... install it!
                        os.system('sudo apt-get install --yes '+apt_cmd)
                else:
                    key = input(thisAppOutput+'Install with APTITUDE: ' + apt_cmd + confirmText)
                    if key == 'y':
                        os.system('sudo apt-get install '+apt_cmd)

    def shell_pre_install_cmd(self):
        # Post INSTALL operations #####################################################
        if len(self.shell_pre_install_cmds) != 0:
            for shell_cmd in self.shell_pre_install_cmds:
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Execute: '+shell_cmd + confirmText)
                if key == 'y':
                    os.system(shell_cmd)
   
    def make_destop_file(self):
        ## Dodajanje program.desktop datoteke v /usr/share/applications/ ################
        if len(self.program_desktop) != 0:
            # test ce je kaj not: sys.stdout.write(self.program_desktop[0])
            # sudo sh -c 'echo "export PATH=\$PATH:/opt/arduino-1.8.1" >> /etc/profile.d/arduino_path.sh'
            if self.auto_install:
                key = 'y'
            else:
                key = input(thisAppOutput+'Naredi menu:'+ menu_desktop + self.program_name+ '.desktop ?'+confirmText)
            if key == 'y':
                #naredi le ce fajl ne obstaja...
                if not os.path.isfile(menu_desktop + self.program_name+ '.desktop'):
                    for menu in self.program_desktop:
                        sudo_txt=[]
                        sudo_txt.append('sudo sh -c ')
                        sudo_txt.append("'echo ")
                        sudo_txt.append('"'+ menu + '"')
                        sudo_txt.append(" >> "+ menu_desktop + self.program_name + ".desktop'")
                        #sys.stdout.write(sudo_txt[0]+sudo_txt[1]+sudo_txt[2]+sudo_txt[3])
                        os.system(sudo_txt[0]+sudo_txt[1]+sudo_txt[2]+sudo_txt[3])

    def shell_post_install_cmd(self):
        # Post INSTALL operations #####################################################
        if len(self.shell_post_install_cmds) != 0:
            for shell_cmd in self.shell_post_install_cmds:
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Execute: '+shell_cmd + confirmText)
                if key == 'y':
                    os.system(shell_cmd)

    def install_DEB_package(self):
        ## Install form DEB package ###################################################
        if (self.deb_package_file !='' or
        (self.deb_package_file_64 != '' and self.arhitecture_64bit ) or
        (self.deb_package_file_32 != '' and self.arhitecture_32bit )):
		#Najprej poglejmo kaksno arhitekturo imamo
            if (self.deb_package_file_64 != '' and self.arhitecture_64bit ):
                sys.stdout.write(thisAppOutput+'Kaze, da imate 64bit arhitekturo...'+escapeColorDefault+'\n')
                temp_deb_package_path = self.deb_package_path_64
                temp_deb_package_file = self.deb_package_file_64
            elif (self.deb_package_file_32 != '' and self.arhitecture_32bit):
                sys.stdout.write(thisAppOutput+'Kaze, da imate 32bit arhitekturo...'+escapeColorDefault+'\n')
                temp_deb_package_path = self.deb_package_path_32
                temp_deb_package_file = self.deb_package_file_32
            else:
                sys.stdout.write(thisAppOutput+'Ne glede na arhitekturo...'+escapeColorDefault+'\n')
                temp_deb_package_path = self.deb_package_path
                temp_deb_package_file = self.deb_package_file
		#-------------------------------------------------
           #ce je vpisan deb paket potem ...
           #najprej preveri, ce ga slucajno ze imamo v Downloadu...
           #ce ne pojdi na internet...
            if not os.path.isfile(download_dir+temp_deb_package_file):
                #ce file ne obstaja gremo gledat na internet...
                sys.stdout.write(thisAppOutput+'Preverjam DEB package...'+escapeColorDefault+'\n')
                os.system('wget --spider -v '+temp_deb_package_path+temp_deb_package_file)
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Prenesi v '+download_dir+ confirmText)
                if key == 'y':
                    os.system('wget '+ temp_deb_package_path + temp_deb_package_file + ' --directory-prefix='+download_dir )
            #pokazi direktorij Download
            if os.path.isfile(download_dir+temp_deb_package_file):
                sys.stdout.write(thisAppOutput+'Nasel:'+escapeColorDefault+'\n')
                os.system('ls -all ' + download_dir + ' | grep ' + temp_deb_package_file)
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Namesti DEB package: ' + temp_deb_package_file + confirmText)
                if key == 'y':
                    os.system('sudo dpkg -i ' + download_dir + temp_deb_package_file)
                    sys.stdout.write(thisAppOutput+'Namestitev koncana...'+escapeColorDefault+'\n')
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Izbrisi datoteko:'
                            + download_dir + temp_deb_package_file+'*'
                            + confirmText)
                if key == 'y':
                    os.system('rm -v ' + download_dir + temp_deb_package_file)
                    #sys.stdout.write(thisAppOutput+'Izprisano:'+escapeColorDefault+'\n')
                    #os.system('ls -all ' + download_dir)
            else:
                sys.stdout.write(thisAppOutput+'Paketa: '+ temp_deb_package_file +' nismo nasli...'+escapeColorDefault+'\n')


    def install_TAR_package(self):
        ## Install form TAR **** special !!! ###########################################
        if (self.tar_package_file !='' or
        (self.tar_package_file_64 != '' and self.arhitecture_64bit ) or
        (self.tar_package_file_32 != '' and self.arhitecture_32bit )):
            #Najprej poglejmo kaksno arhitekturo imamo
            if (self.tar_package_file_64 != '' and self.arhitecture_64bit ):
                sys.stdout.write(thisAppOutput+'Kaze, da imate 64bit arhitekturo...'+escapeColorDefault+'\n')
                temp_tar_package_path = self.tar_package_path_64
                temp_tar_package_file = self.tar_package_file_64
            elif (self.tar_package_file_32 != '' and self.arhitecture_32bit):
                sys.stdout.write(thisAppOutput+'Kaze, da imate 32bit arhitekturo...'+escapeColorDefault+'\n')
                temp_tar_package_path = self.tar_package_path_32
                temp_tar_package_file = self.tar_package_file_32
            else:
                sys.stdout.write(thisAppOutput+'Ne glede na arhitekturo...'+escapeColorDefault+'\n')
                temp_tar_package_path = self.tar_package_path
                temp_tar_package_file = self.tar_package_file
            #Najprej zloadas tar file ... izi bizi...
            if not os.path.isfile(download_dir+temp_tar_package_file):
                #ce file ne obstaja gremo gledat na internet...
                sys.stdout.write(thisAppOutput+'Preverjam TAR package...'+escapeColorDefault+'\n')
                os.system('wget --spider -v '+temp_tar_package_path+temp_tar_package_file)
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Prenesi v '+download_dir+ '?'+confirmText)
                if key == 'y':
                    os.system('wget '+ temp_tar_package_path + temp_tar_package_file + ' --directory-prefix='+download_dir )
            #pokazi direktorij Download
            if os.path.isfile(download_dir+temp_tar_package_file):
                sys.stdout.write(thisAppOutput+'Nasel:'+escapeColorDefault+'\n')
                os.system('ls -all ' + download_dir + ' | grep ' + temp_tar_package_file)
                if self.tar_destination == '':
                    if self.auto_install:
                        key = 'y'
                    else:
                        key = input(thisAppOutput+'Razpakiraj TAR package: '+ temp_tar_package_file +' v ' + download_dir + '?'+confirmText)
                    if key == 'y':
                        os.system('tar -xvf '+ download_dir+temp_tar_package_file+' --directory '+ download_dir)
                else:
                    if self.auto_install:
                        key = 'y'
                    else:
                        key = input(thisAppOutput+'Razpakiraj TAR package: '+ temp_tar_package_file +' v ' + self.tar_destination + '?'+confirmText)
                    if key == 'y':
                        if not os.path.isdir(self.tar_destination):
                            #ce dir se ne obstaja ga ustvari...
                            os.system('sudo mkdir ' + self.tar_destination)
                        os.system('sudo tar -xvf '+download_dir+temp_tar_package_file+' --directory '+ self.tar_destination)
                # Izbrisi kar smo zloadali... da pocistimo za seboj...
                if self.auto_install:
                    key = 'y'
                else:
                    key = input(thisAppOutput+'Izbrisi datoteko:'+ download_dir + temp_tar_package_file+'*'+ confirmText)
                if key == 'y':
                    os.system('rm -v ' + download_dir + temp_tar_package_file+'*')
                    #sys.stdout.write(thisAppOutput+'Izbrisano:'+escapeColorDefault+'\n')
                    #os.system('ls -all ' + download_dir)
            else:
            	sys.stdout.write(thisAppOutput+'Datoteke: '+download_dir+temp_tar_package_file+' nismo nasli...'+escapeColorDefault+'\n')
            
            ## INSTALATION SOURCE CODE #######################################################
            	# ok sedaj naj bi bilo razpakirano... kjerkoli pac ze...
            	#ja nic zej pa ce je treba se kako EXTRA CMD narest!!!
            	#naprimer kak make, make install, itd
            	#skratka izvrsimo komande, ki jih najdemo v :
            	#self.tar_extra_cmds = ['make','make install']
            if len(self.tar_extra_cmds) != 0:
                for extra_cmd in self.tar_extra_cmds:
                    key = input(thisAppOutput+'execute:'+extra_cmd+confirmText)
                    if key == 'y':
                        os.system(extra_cmd)


    def version_check(self):
        # KONEC INSTALACIJE samo se navodila in verzija check! ########################
    #    if len(self.check_version_cmd) > 0:
    #        pckg_name = self.check_version_cmd
    #    else:
    #        if (len(self.apt_get_install) > 0) or (len(self.arch_pacman_cmds) > 0):
    #            if len(self.arch_yaourt_cmds) < len(self.arch_pacman_cmds):
    #                pckg_name = self.arch_pacman_cmds[0]
    #            else:
    #                pckg_name = self.arch_yaourt_cmds[0]
    #    info_installed_file = os.popen('pacman -Qi ' + pckg_name)
    #    info_installed_text = info_installed_file.read()
    #    if len(info_installed_text) > 1:
    #        # it is alredy installed...
    #        sys.stdout.write(thisAppOutput+'Paket : ' + pckg_name + ' je ze namescen.' + escapeColorDefault + '\n')
    #        sys.stdout.write(escapeColorInstalled + info_installed_text + escapeColorDefault+'\n')
    #        return True
    #    else:
    #        # it is not installed...
         return False

    def show_notes(self):
        if self.notes != '':
            sys.stdout.write(thisAppOutput+self.notes+''+escapeColorDefault+'\n')

    def install(self):
        sys.stdout.write('###########################################################\n'
                         + '# Postopek instalacije programa \n'
                         + '# '+escapeColorCmd + self.program_name+''+escapeColorDefault+'\n'
                         + '-----------------------------------------------------------\n')
        if self.description != '':
            new_start = 0
            last_presledek = 0
            for n in range(1, len(self.description)):
                presledek = self.description.find(' ', last_presledek+1, n)
                # testing izpis ne dela najbolje...
                new_line = self.description.find('\n', last_presledek+1, n)
                if (new_line > last_presledek):
                    print(escapeColorDefault+self.description[new_start:new_line])
                    last_presledek = new_line + 1
                    new_start = new_line + 1

                if (new_line > new_start + 59):
                    print(escapeColorDefault+self.description[new_start:last_presledek])
                    new_start = last_presledek + 1

                if (presledek > new_start + 59):
                    print(escapeColorDefault+self.description[new_start:last_presledek])
                    new_start = last_presledek + 1
                else:
                    if (presledek > 0):
                        last_presledek = presledek

            sys.stdout.write(escapeColorDefault+self.description[new_start:]+''+escapeColorDefault+'\n'
                             + '###########################################################\n')
        # 
        self.shell_pre_install_cmd()
        self.apt_get_install()
        self.install_DEB_package()
        self.install_TAR_package()
        self.shell_post_install_cmd()
        self.make_destop_file()
        self.show_notes()
        sys.stdout.write(thisAppOutput+'Pritisni [ENTER] za nadaljevanje...'+escapeColorDefault+'\n')

## PROGRAMI ###############################################
## GIT ####################################################
GIT = NovProgram()
GIT.program_name = 'git'  # ime naj bo brez presledkov
GIT.category = 'Development'
GIT.description = 'Protokol za skrbno spremljanje verzij'\
                'razvojnih programov.'  # neko besedilo za opis
GIT.apt_get_install_cmds = ['git']
GIT.notes = ''
GIT.shell_post_install_cmds = [
    'git config --global user.email "david.rihtarsic@gmail.com"',
    'git config --global user.name "davidrihtarsic"',
    'git clone https://github.com/davidrihtarsic/Arduino-Data-Acquisition-Device.git ~/Files/GitHub_noSync/Arduino-Data-Acquisition-Device',
    'git clone https://github.com/davidrihtarsic/ArchLabs.git ~/Files/GitHub_noSync/ArchLabs',
    'git clone https://github.com/davidrihtarsic/InstallMyApps.git ~/Files/GitHub_noSync/InstallMyApps',
    'git clone https://github.com/davidrihtarsic/myLinuxNotes.git ~/Files/GitHub_noSync/myLinuxNotes',
    'git clone https://github.com/davidrihtarsic/Korad3005p.git ~/Files/GitHub_noSync/Korad3005p',
    'git clone https://github.com/davidrihtarsic/BunsenLab.git ~/Files/GitHub_noSync/BunsenLabs',
    'git clone https://github.com/davidrihtarsic/RobDuino.git ~/Files/GitHub_noSync/RobDuino',
    'git clone https://github.com/davidrihtarsic/ArduinoCNC-DCmotors.git ~/Files/GitHub_noSync/CNC-ArduinoDCmotors']
GIT.auto_install = True
vsi_programi.append(GIT)

## oh-my-zsh ####################################################
OH_MY_ZSH = NovProgram()
OH_MY_ZSH.program_name = 'oh-my-zsh'  # ime naj bo brez presledkov
OH_MY_ZSH.category = 'Development'
OH_MY_ZSH.description = 'Super kul bash....'\
                '...pameten, ko svina.'  # neko besedilo za opis
OH_MY_ZSH.shell_pre_install_cmds = [
        'sudo apt-get install zsh',
	'git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh',
	'cd ~/.oh-my-zsh && sudo sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"',
	'chsh -s /bin/zsh']
OH_MY_ZSH.notes = ''
OH_MY_ZSH.auto_install=True
vsi_programi.append(OH_MY_ZSH)

## VIM ####################################################
VIM = NovProgram()
VIM.program_name = 'vim'  # ime naj bo brez presledkov
VIM.category = 'Development'
VIM.description = 'VIM like file manager.'  # neko besedilo za opis
VIM.apt_get_install_cmds = ['vim-gtk']
VIM.shell_post_install_cmds = [
	'git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim',
	'sudo apt-get install exuberant-ctags',
    'sudo apt-get font-symbola']
VIM.notes = ''
VIM.auto_install = True
vsi_programi.append(VIM)

## Gimp ####################################################
Gimp = NovProgram()
Gimp.program_name = 'Gimp'  # ime naj bo brez presledkov
Gimp.category = 'Development'
Gimp.description = 'Gimp - orodje za obdelavo birtnih slik.'  # neko besedilo za opis
Gimp.apt_get_install_cmds = ['gimp']
Gimp.notes = ''
Gimp.auto_install = True
vsi_programi.append(Gimp)

## PopcornTime ####################################################
PopcornTime = NovProgram()
PopcornTime.program_name = 'PopcornTime'  # ime naj bo brez presledkov
PopcornTime.category = 'Multimedia'
PopcornTime.description = 'PopcornTime.'  # neko besedilo za opis
PopcornTime.notes = ''
PopcornTime.tar_package_path_64='https://dl.popcorn-time.to/'
PopcornTime.tar_package_file_64='Popcorn-Time-linux64.tar.gz'
PopcornTime.tar_destination=opt_dir+PopcornTime.program_name
PopcornTime.program_desktop=[
        '[Desktop Entry]',
        'Version=1.0',
        'Name=PopcornTime (Movies, Cartoons, Series...',
        'Exec=/opt/PopcornTime/Popcorn-Time',
        'Icon=',
        'Terminal=false',
        'Type=Application',
        'Categories=Enterteinment;'
        ]
PopcornTime.auto_install = True
vsi_programi.append(PopcornTime)

## Arduino ####################################################
Arduino = NovProgram()
Arduino.program_name = 'Arduino'  # ime naj bo brez presledkov
Arduino.category = 'Development'
Arduino.description = 'Programming IDE for Arduino boards...'  # neko besedilo za opis
Arduino.notes = ''
Arduino.tar_package_path_64='https://downloads.arduino.cc/'
Arduino.tar_package_file_64='arduino-nightly-linux64.tar.xz'
Arduino.tar_destination=opt_dir
Arduino.auto_install = True
Arduino.program_desktop = [
        '[Desktop Entry]',
        'Version=1.0',
        'Name=Arduino IDE',
        'Exec=/opt/arduino-nightly/arduino',
        'Icon=openbox.png',
        'Terminal=false',
        'Type=Application',
        'Categories=Development;'
        ]
vsi_programi.append(Arduino)

## Atom ####################################################
Atom = NovProgram()
Atom.program_name = 'Atom'  # ime naj bo brez presledkov
Atom.category = 'Office'
Atom.description = 'A hackable text editor for the 21st Century.'  # neko besedilo za opis
Atom.shell_pre_install_cmds = []
Atom.apt_get_install_cmds = []
Atom.deb_package_path_64 ='https://atom-installer.github.com/v1.33.0/'
Atom.deb_package_file_64 ='atom-amd64.deb'
Atom.shell_post_install_cmds = [
    'sudo apt --fix-broken install',
    'sudo apt install python3-pip',
    'sudo python3 -m pip install "python-language-server[all]"',
    'apm install ide-python',
    'apm install atom-ide-ui',
    'apm install symbols-tree-view',
    'apm install vim-mode',
    'apm install script',
    'apm install language-markdown',
    'apm install markdown-table-editor',
    'apm install relative-numbers']
Atom.auto_install = True
Atom.notes = '!! NASTAVITI JE POTREBNO: Settings -> Packages -> ide-python [Python executables: python3] !!!'
vsi_programi.append(Atom)

## Google_Chrome ####################################################
Google_Chrome = NovProgram()
Google_Chrome.program_name = 'Google_Chrome'  # ime naj bo brez presledkov
Google_Chrome.category = 'Office'
Google_Chrome.description = 'Google Chrome'  # neko besedilo za opis
Google_Chrome.shell_pre_install_cmds = []
Google_Chrome.apt_get_install_cmds = []
Google_Chrome.deb_package_path_64 ='https://dl.google.com/linux/direct/'
Google_Chrome.deb_package_file_64 ='google-chrome-stable_current_amd64.deb'
Google_Chrome.auto_install = True
Google_Chrome.notes = ''
vsi_programi.append(Google_Chrome)

## Thunderbird ####################################################
Thunderbird = NovProgram()
Thunderbird.program_name = 'Thunderbird'  # ime naj bo brez presledkov
Thunderbird.category = 'Office'
Thunderbird.description = 'Thunderbird is an email/news/chat clienth a possible RSS feed aggregation developed by Mozilla.'  # neko besedilo za opis
Thunderbird.shell_pre_install_cmds = []
Thunderbird.apt_get_install_cmds = [
        'thunderbird']
Thunderbird.shell_post_install_cmds = []
Thunderbird.auto_install = True
Thunderbird.notes = ''
vsi_programi.append(Thunderbird)

## Nemo ####################################################
Nemo = NovProgram()
Nemo.program_name = 'Nemo'  # ime naj bo brez presledkov
Nemo.category = 'Office'
Nemo.description = 'Nemo - File manager'  # neko besedilo za opis
Nemo.shell_pre_install_cmds = []
Nemo.apt_get_install_cmds = [
        'nemo']
Nemo.shell_post_install_cmds = []
Nemo.auto_install = True
Nemo.notes = ''
vsi_programi.append(Nemo)

## Zathura ####################################################
Zathura = NovProgram()
Zathura.program_name = 'Zathura'  # ime naj bo brez presledkov
Zathura.category = 'Office'
Zathura.description = 'Zathura PEF reader'  # neko besedilo za opis
Zathura.shell_pre_install_cmds = []
Zathura.apt_get_install_cmds = [
        'zathura']
Zathura.shell_post_install_cmds = []
Zathura.auto_install = True
Zathura.notes = ''
vsi_programi.append(Zathura)

## PrinterSupport ####################################################
PrinterSupport = NovProgram()
PrinterSupport.program_name = 'PrinterSupport'  # ime naj bo brez presledkov
PrinterSupport.category = 'Office'
PrinterSupport.description = 'PrinterSupport PEF reader'  # neko besedilo za opis
PrinterSupport.shell_pre_install_cmds = []
PrinterSupport.apt_get_install_cmds = [
        'task-print-server']
PrinterSupport.shell_post_install_cmds = []
PrinterSupport.auto_install = True
PrinterSupport.notes = ''
vsi_programi.append(PrinterSupport)

## RANGER ####################################################
RANGER = NovProgram()
RANGER.program_name = 'ranger'  # ime naj bo brez presledkov
RANGER.category = 'System'
RANGER.description = 'System status'  # neko besedilo za opis
RANGER.shell_pre_install_cmds = [
        'git clone https://github.com/ranger/ranger.git ~/Downloads/ranger',
        'cd ~/Downloads/ranger && sudo make install',
        'sudo apt-get install w3m-img']
RANGER.notes = ''
RANGER.auto_install=True
vsi_programi.append(RANGER)

# LinkDotFiles ########################################################
LinkDotFiles = NovProgram()
LinkDotFiles.program_name = 'LinkDotFiles'
LinkDotFiles.category = 'System'
LinkDotFiles.description = 'Make link for any files in ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/...'
LinkDotFiles.shell_pre_install_cmds = ['/home/david/Files/GitHub_noSync/BunsenLabs/MyDotFiles/bin/system/makeSymbolicLinks.sh']
LinkDotFiles.auto_install = True
vsi_programi.append(LinkDotFiles)

# OpenBoxMenu ########################################################
#OpenBoxMenu = NovProgram()
#OpenBoxMenu.program_name = 'OpenBoxMenu'
#OpenBoxMenu.category = 'System'
#OpenBoxMenu.description = 'Make link for any files in ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/...'
#OpenBoxMenu.shell_pre_install_cmds = [
#        'mv ~/.config/openbox/menu.xml ~/.config/openbox/menu_original.xml',
#        'cp ~/.config/openbox/menu_template.xml ~/.config/openbox/menu.xml',
#        'sudo git clone https://github.com/woho/openbox-menu.git '+opt_dir+'openbox-menu',
#        '/opt/openbox-menu/obmenu.py'
#        ]
#OpenBoxMenu.auto_install = True
#vsi_programi.append(OpenBoxMenu)

## FreeCAD ####################################################
FreeCAD = NovProgram()
FreeCAD.program_name = 'FreeCAD'  # ime naj bo brez presledkov
FreeCAD.category = 'Graphics'
FreeCAD.description = 'FreeCAD is an open-source parametric 3D modeler made primarily to design real-life objects of any size. Parametric modeling allows you to easily modify your design by going back into your model history and changing its parameters.'  # neko besedilo za opis
FreeCAD.shell_pre_install_cmds = []
FreeCAD.apt_get_install_cmds = [
        'freecad']
FreeCAD.shell_post_install_cmds = []
FreeCAD.auto_install = True
FreeCAD.notes = ''
vsi_programi.append(FreeCAD)

## Neofetch ####################################################
Neofetch = NovProgram()
Neofetch.program_name = 'Neofetch'  # ime naj bo brez presledkov
Neofetch.category = 'Other'
Neofetch.description = 'Neoftech is a cross-platform and easy-to-use system information command line script that collects your Linux system information and display it on the terminal next to an image, it could be your distributions logo or any ascii art of your choice.'  # neko besedilo za opis
Neofetch.shell_pre_install_cmds = []
Neofetch.apt_get_install_cmds = [
        'neofetch']
Neofetch.shell_post_install_cmds = []
Neofetch.auto_install = False
Neofetch.notes = ''
vsi_programi.append(Neofetch)

## Rofi ####################################################
Rofi = NovProgram()
Rofi.program_name = 'Rofi'  # ime naj bo brez presledkov
Rofi.category = 'Office'
Rofi.description = 'Rofi is an email/news/chat clienth a possible RSS feed aggregation developed by Mozilla.'  # neko besedilo za opis
Rofi.shell_pre_install_cmds = []
Rofi.apt_get_install_cmds = [
        'rofi']
Rofi.shell_post_install_cmds = []
Rofi.auto_install = True
Rofi.notes = ''
vsi_programi.append(Rofi)

## JGMENU ####################################################
JGMENU = NovProgram()
JGMENU.program_name = 'JGMENU'  # ime naj bo brez presledkov
JGMENU.category = 'Other'
JGMENU.description = 'System status'  # neko besedilo za opis
JGMENU.shell_pre_install_cmds = [
        'git clone https://github.com/johanmalm/jgmenu.git ~/Downloads/jgmenu',
        'cd ~/Downloads/jgmenu && ./scripts/install-debian-dependencies.sh',
        'cd ~/Downloads/jgmenu && make',
        'cd ~/Downloads/jgmenu && make prefix=$HOME install']
JGMENU.notes = ''
vsi_programi.append(JGMENU)

## FEH ####################################################
FEH = NovProgram()
FEH.program_name = 'FEH'  # ime naj bo brez presledkov
FEH.category = 'Other'
FEH.description = 'System status'  # neko besedilo za opis
FEH.apt_get_install_cmds = ['feh']
FEH.notes = ''
FEH.auto_install=True
vsi_programi.append(FEH)

## NERDFONT ####################################################
NERDFONT = NovProgram()
NERDFONT.program_name = 'NERDFONT'  # ime naj bo brez presledkov
NERDFONT.category = 'Other'
NERDFONT.description = 'NERD-FONT like file manager.'  # neko besedilo za opis
NERDFONT.apt_get_install_cmds = []
NERDFONT.shell_post_install_cmds = [
        'sudo apt-get install gucharmap'
        'git clone https://github.com/ryanoasis/nerd-fonts.git ~/Downloads/nerd-font',
        'cd ~/Downloads/nerd-font && ./install.sh UbuntuNerdFont']
NERDFONT.notes = ''
NERDFONT.auto_install=True
vsi_programi.append(NERDFONT)

## I3 ####################################################
# tudi vse kar je potrebno za moj system
I3 = NovProgram()
I3.program_name = 'i3'  # ime naj bo brez presledkov
I3.category = 'Other'
I3.description = 'System status'  # neko besedilo za opis
I3.shell_pre_install_cmds = [
        # i3 window manager
        'sudo apt-get install i3 suckless-tools',
        # i3 orodna vrstica
        'sudo apt-get install i3blocks',
        'git clone https://github.com/vivien/i3blocks-contrib ~/.config/i3blocks',
        'cd ~/.config/i3blocks && cp config.example config',
        # menu za programe (lahko uporabljas tudi dmenu
        'sudo apt install rofi',
        #xbacklight ( za osvetlitev zaslona _Asus FIX)
        #'sudo apt-get install xbacklight'
        'sudo touch /etc/udev/rules.d/backlight.rules',
        'cat ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/.config/i3/kbd_backlight.rules | sudo tee /etc/udev/rules.d/backlight.rules',
        'cat ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/.config/i3/lcd_backlight.rules | sudo tee -a /etc/udev/rules.d/backlight.rules',
        'sudo chmod a+w /sys/class/leds/asus::kbd_backlight/brightness',
        'sudo chmod a+w /sys/class/backlight/intel_backlight/brightness',
#touchpad guestures
        'cat ~/Files/GitHub_noSync/BunsenLabs/MyDotFiles/.config/i3/touchPad_guestures.conf | sudo tee -a /usr/share/X11/xorg.conf.d/70-synaptics.conf',
        # symbola fonts and emojis
        'sudo apt-get install fonts-symbola ttf-ancient-fonts-symbola ttf-marvosym fonts-opensymbol fonts-powerline fonts-font-awesome',
        # ffmpeg for resording screens...
        'sudo apt-get install ffmpeg'
        ]
I3.notes = ''
I3.auto_install=True
vsi_programi.append(I3)


#################################################################
#################################################################
# find programs and categorize them
# Force Auto and System as first
all_categorys = ['Accesories', 'Development', 'Office', 'Internet', 'Graphics', 'Multimedia', 'Other', 'System']
category_programs = [0, 0, 0, 0, 0, 0, 0, 0]
all_program_manes = []
for program in vsi_programi:
    all_program_manes.append(program.program_name)
    if program.category in all_categorys:
        i = all_categorys.index(program.category)
        category_programs[i] += 1
    else:
        all_categorys.append(program.category)
        category_programs.append(1)

def makeAllProgramForms():
    global allForms
    allForms = []
    global editProgramms
    editProgramms = []
    global colons
    x = 0
    # y = 4
    dx = 28  # max od program name
    # terminal = os.get_terminal_size()
    # width = terminal.columns
    # colons = width//

    colons = 2
    if colons == 1:
        dy = category_programs[0] + 1
    else:
        dy = max(category_programs)+1  # max od category_programs
    global programID
    programID = 0
    for category in all_categorys:
        col = len(allForms) % colons
        row = len(allForms)//colons
        x = col * (dx + 1) + 2
        if len(allForms) > colons:
            # smo že v 1.,2.,3.. vrsti
            y = allForms[len(allForms)-colons].y + allForms[len(allForms)-colons].dy
        else:
            # smo še v 0. vrsti
            y = (dy * row) + 1
        dy = 4 + max(category_programs[n] for n in range((row*colons), ((row*colons)+colons)))
        allForms.append(Form(category, x, y, dx, dy))
        # filaj programe po kategorijah
        nthCategoryProgram = 0
        for program in vsi_programi:
            if program.category == all_categorys[len(allForms)-1]:
                programID += 1
                nthCategoryProgram += 1
                program.index = programID
                editX = allForms[len(allForms)-1].x + 2
                editY = allForms[len(allForms)-1].y + nthCategoryProgram + 1
                editText = '(' + str(programID) + ')'
                editProgramms.append(Edit(editText, editX, editY))
                editProgramms[programID-1].new_value(program.program_name)

def MakeHelpForm():
    HotKeys = ['--Menu------------------',
               'n      - inst. program',
               '[u]    - Update & Upgrade',
               '[ENTER]- MAIN MENU',
               '[q]    - EXIT']

    x = allForms[0].x + (allForms[0].dx + 1) * colons
    y = allForms[0].y
    dx = allForms[0].dx
    dy = 0
    row = len(allForms)//colons
    for n in range(0, row):
        dy += allForms[n*colons].dy
    allForms.append(Form('Auto', x, y, dx, dy))

    nthCategoryProgram = 0
    for program in vsi_programi:
            if program.auto_install:
                global programID
                programID += 1
                nthCategoryProgram += 1
                program.index = programID
                editX = allForms[len(allForms)-1].x + 2
                editY = allForms[len(allForms)-1].y + nthCategoryProgram + 1
                editText = '(' + str(programID) + ')'
                editProgramms.append(Edit(editText, editX, editY))
                editProgramms[programID-1].new_value(program.program_name)

    t_Keys = []
    x = allForms[len(allForms)-1].x
    y = allForms[len(allForms)-1].y + allForms[len(allForms)-1].dy - len(HotKeys) - 2
    for n in range(0, len(HotKeys)):
        t_Keys.append(Text(HotKeys[n], x + 2, y + n + 1))

## MAIN PROGRAM ##############################################
def Main():
    makeAllProgramForms()
    MakeHelpForm()
    y = allForms[len(allForms) - 1].dy + 1
    setCursor(1, y)

key = ''
cls()
Main()
Main()
# while (editCmd.value != 'q'):
while (key != 'q'):
    key = input('Cmd::')
    # programe_index=(i for i in range(50))
    # next(programe_index)
    if key == '':
        cls()
        Main()
    else:
        # preglej vse programe...
        try:
            prog_id = int(key)-1
            for program in vsi_programi:
                if editProgramms[prog_id].value == str(program.program_name):
                    program.install()
                    key = ''
        except ValueError:
            if key == 'u':
                os.system('sudo pacman -Syu')
                os.system('yaourt -Syua')
            elif key in all_categorys:
                for program in vsi_programi:
                    if program.category == key:
                        program.install()
            elif key == 'Auto':
                for program in vsi_programi:
                    if program.auto_install:
                        program.install()
            else:
                os.system(key)
cls()

