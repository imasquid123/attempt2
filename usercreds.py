class UserCredentialExchange:
#put creds in holder
	def putusercredentials(usr_credential_holder):
		usercred = store.locked_get()
    	usercred.locked_put(usr_credential_holder)
