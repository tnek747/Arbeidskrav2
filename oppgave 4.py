
"""
Created on Fri Nov 22 20:41:17 2024

@author: KoKe
"""
# Dict med data
data= {
       "Norge": ["Oslo",0.634],
       "England": ["London",8.982],
       "Frankrike": ["Paris",2.161],
       "Italia": ["Roma",2.873]
       }
#variable om å legge til data i listen
i = "0"

#Spørr bruker hvilket land som Hen hønsker info om
l=input("Hvilket land tenker du på? ")


#b = list(data.keys())

#Sjekker om landet ligger i dict data.
if l in data:
    print(l, "Har jeg denne informasjonen om")
    #Skiver ut info om landet som er skrevet inn hvos det er i data
    print(data[l][0],"Hovedstaden i", l,"og det er", data[l][1],"mill. innbyggere i",data[l][0])

#Har ikke info i dict så spørr om vi skal legge det til    
else:
    print(l, "kjenner jeg ikke ikke til.")
    i=input ("Ønsker du å legge det til? Y/N ")  
 
 #Bruker ønsker å legge det til   
if i == "Y":
    print("legg inn informasjon om", l," under nå")
    k=input("Hovedstaden? " )
    p=input("Antall inbyggere? ")
    data[l] = [k,p]
    i == "0"       
    print(data)
    
#Bruker ønsker ikke å legge det til     
elif i == "N": 
            print("Da var er oppgave 4 ferdig og du kan gå til oppgave 5. tusen takk")