# eind_project_api_development
eindproject voor het vak api_development


# Screen GitHub Docs
![afbeelding](https://user-images.githubusercontent.com/57671114/211197785-7cd911b5-d397-4225-a32d-6c76476abc64.png)
![afbeelding](https://user-images.githubusercontent.com/57671114/211198686-87fba841-b44e-49f7-8d4d-5c80142205e8.png)


# Screen token-endpoint
![afbeelding](https://user-images.githubusercontent.com/57671114/211198292-c67494bc-7e85-4230-a25b-da102b019a2b.png)

# Screens user-endpoints
GET /USERS, deze endpoint geeft alle users terug. Er is ook een query parameter aanwezig zodat je kan kiezen (bv. van 1-100). Deze endpoint 'required' ook een token, je moet dus eerst aanmelden met een bestaande user(of user aanmaken met post-endpoint) om een token te verkrijgen.
![afbeelding](https://user-images.githubusercontent.com/57671114/211198348-8df2dd07-e38b-4de1-b067-9098df7d156d.png)

POST /USERS, deze endpoint geeft de optie om een nieuwe user aan te maken.
![afbeelding](https://user-images.githubusercontent.com/57671114/211198575-8ffbf8ad-f6b2-465c-a606-b0f4e069b219.png)

GET /USERS/ME, deze endpoint geeft de user terug waarmee je op die moment aangemeld bent (token) .
![afbeelding](https://user-images.githubusercontent.com/57671114/211198726-9d4fa2f9-80f8-4486-8f3b-c17306953447.png)

GET /USERS/{USER_ID}, deze endpoint geeft de mogelijkheid om 1 bepaalde user terug te geven op basis van id. Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211198826-6f9c8f6b-5871-42f6-adc6-e9a5e2f2be12.png)

GET /TEAMS, deze endpoint geeft de mogelijkheid om alle teams terug te geven. Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211199123-3f24f98f-7247-4494-b4a9-bbc12bb5b433.png)

POST /TEAMS, deze endpoint geeft de mogelijkheid om een team aan te maken. Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211199314-d798bc6e-534c-4347-897d-d6f505cd44d7.png)

GET /TEAMS/{TEAM_ID}, deze endpoint geeft de mogelijkheid om 1 bapaald team terug te geven op basis van id. Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211199387-15ae4a25-8b0d-4999-ac3c-53dfcfeb1fe0.png)
