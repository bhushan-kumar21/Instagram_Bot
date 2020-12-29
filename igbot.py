from time import sleep
from selenium import webdriver


c=0  # counter for minimun posts

class igbot:
    def __init__(self,username,password):

        self.browser=webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
        self.browser.implicitly_wait(5)
        self.browser.get('https://www.instagram.com/')

        self.username=username
        self.passowrd=password
        self.browser.find_element_by_css_selector("input[name='username']")\
            .send_keys(username)
        self.browser.find_element_by_css_selector("input[name='password']")\
            .send_keys(password)
        sleep(5)
        self.browser.find_element_by_xpath("//button[@type='submit']")\
            .click()
        sleep(2)

        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        self.browser.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
            .click()

    def search(self,searchelement):
        self.searchelement=searchelement
        self.browser.find_element_by_css_selector("input[placeholder='Search']")\
            .send_keys(searchelement)  #css_path for search box and to type the search element
        sleep(5)
        self.browser.find_element_by_class_name("yCE8d")\
            .click()  
        sleep(2)
        self.browser.find_element_by_class_name("_9AhH0")\
                .click()  

    def like(self):
        self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')\
            .click()   # xpath for like button 

    def comment(self,comm):
        self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')\
            .click()   # selecting text box
        sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')\
            .send_keys(comm)    #passing the comment 
        sleep(2)    
        self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button')\
            .click()         # submitting the comment 

   

    def nextpic(self):
        global c
        self.like()                       # like function 
        sleep(2)
        self.comment('This_is_a_bot')     # comment function
        sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")\
        .click()
        sleep(2)
        self.like()
        sleep(2)
        while c < 5: # set minimum post value 
                self.browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')\
                    .click()
                sleep(2)
                self.like()
                sleep(2)
                # self.comment('This_is_a_bot') #  uncomment this to comment multiple times
                c+=1
                self.browser.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")\
                    .click() 
                sleep(2)     
                self.like()
                sleep(2)     


bot1=igbot('email/userid','passowrd')
bot1.search("user/page to search")
bot1.nextpic() 


