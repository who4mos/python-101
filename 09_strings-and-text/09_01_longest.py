# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
# added an additional backslash (\), python was complaining about the escape sequence
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

print(len(longest_german_word))    # 61
print(len(longest_hungarian_word)) # 44
print(len(longest_finnish_word))   # 61
print(len(strong_password))        # 62 - longest
