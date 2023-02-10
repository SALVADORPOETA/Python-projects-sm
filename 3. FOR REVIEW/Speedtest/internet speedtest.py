# Modificaciones:

# Cuando le doy a la opción 3, me retorna un 0 pero en el otro speedtest me retorna 79.955
# Ahora me retorna este problema: speedtest.ConfigRetrievalError: HTTP Error 403: Forbidden


import speedtest

st = speedtest.Speedtest()

option = int(input('''What speed do you want to measure: 

1) Download Speed

2) Upload Speed

3) Ping

Your Choice: '''))

if option==1:
	print(st.download()/(1025*1025), "Mbps")
elif option==2:
	print(st.upload()/(1025*1025), "Mbps")
elif option==3:
	servernames=[]
	st.get_servers(servernames)
	print(st.results.ping)
else:
	print("Please enter correct option!")