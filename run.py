import time
import btc_api
import text

def main():
	while True:
		price = btc_api.ppfunc()
		text.show_text(price)
		time.sleep(5)	
		
main()
