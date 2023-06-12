# database_bot_for_photo_number_01
this telegram bot serves as a database for photos. The principle of its operation is that it creates for each new user an account in which the user can store their photos, receive them,
and delete them. To create an account, I use ordinary folders in the name of which the user's name and password are written through the "_" sign, which the user comes up with himself.
At the beginning, the bot will offer to either log in or register, registration takes place as the user enters the name and password, for example: Korazon 123, and after that the Korazon_123 folder is created,
which we enter after registration. When logging into the account, the user enters a name and password, for example, Corazon 321, and this name and password are searched in the name of the folders,
if they are located, then we go into it where the data is stored. Already in the user's account, there are three commands: push, get, remove. with push, the user must send the name of the photo
and the photo itself, after which a photo is added to the folder of the account into which we entered, in the name of which the user sent us the name, with get and remove, the user simply sends
the name of the photo with get, the specified photo is sent to the user with remove, it is deleted.There are also commands stop push, stop get, stop remove if you change your mind in the process.
There is also a /exit command that deletes all messages in the chat and throws the user out of the account in the folder all changes are saved.

There are disadvantages here: the bot works from the computer on which the code is running,
photos are saved in poor quality, and the code works fine only when one person uses it and then
exits the account, that is, prescribes / exit. In the future, I plan to fix all these disadvantages.
