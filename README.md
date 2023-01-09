# eind_project_api_development
Voor het eindproject van API Development maakte ik een gevanceerdere versie van mijn basisproject. Het thema van mij api is dus opnieuw de champions league. De api is nu wel veel professioneler. Ze is namelijk uitgerust met meerdere path en query parameters, en een oauth + hashing systeem.

Vervolgens koos ik er ook nog voor om een aantal tests te schrijven voor de get-endpoints. Deze plaatste ik in het mapje pytests.

Ik had ook nog een paging gedaan om 4.1 en 5.1 te doen maar voor deze dingen moest je een account aanmaken en dit lukte echter niet bij mij.

Het zou kunnen zijn dat de api op okteto cloud niet beschikbaar is omdat ik merk dat na 2 dagen, deze in slaapmodus gaat. Moest dit zo zijn kan u mij altijd contacteren en dan deploy ik hem opnieuw.

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

GET /USERS/{USER_ID}, deze endpoint geeft de mogelijkheid om 1 bepaalde user terug te geven op basis van id (path parameter). Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211198826-6f9c8f6b-5871-42f6-adc6-e9a5e2f2be12.png)

GET /TEAMS, deze endpoint geeft de mogelijkheid om alle teams terug te geven. Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211199123-3f24f98f-7247-4494-b4a9-bbc12bb5b433.png)

POST /TEAMS, deze endpoint geeft de mogelijkheid om een team aan te maken. Net zoals de user-endpoint heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211199314-d798bc6e-534c-4347-897d-d6f505cd44d7.png)

GET /TEAMS/{TEAM_ID}, deze endpoint geeft de mogelijkheid om 1 bapaald team terug te geven op basis van id (path parameter). Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![afbeelding](https://user-images.githubusercontent.com/57671114/211199387-15ae4a25-8b0d-4999-ac3c-53dfcfeb1fe0.png)

GET /SPELERS, deze endpoint geeft de mogelijkheid om alle spelers terug te geven. Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![image](https://user-images.githubusercontent.com/57671114/211324453-7849852f-0695-4057-be22-09ac18a6b924.png)

PUT /SPELERS, deze endpoint geeft de mogelijkheid om een bepaalde speler aan te passen. Net zoals de user-endpoint heeft deze een token nodig.
Deze endpoint werkt echter niet, ik geraakte niet voorbij deze error.
![image](https://user-images.githubusercontent.com/57671114/211326457-6067e912-c8fe-4411-9dbe-6695b004821d.png)

POST /SPELERS, deze endpoint geeft de megelijkheid om een speler aan te maken. Net zoals de user-endpoint heeft deze een token nodig.
![image](https://user-images.githubusercontent.com/57671114/211327187-ebc7a853-c18d-45be-8e2b-3aac2f0d586f.png)

DELETE /SPELERS, deze endpoint geeft de megelijkheid om een speler te verwijderen. Net zoals de user-endpoint heeft deze een token nodig.
Deze endpoint werkt echter niet, ik geraakte niet voorbij deze error.
![image](https://user-images.githubusercontent.com/57671114/211330636-90270479-afda-4678-b561-4abc3770e438.png)

GET /SPELERS/{SPELER_ID}, deze endpoint geeft de mogelijkheid om 1 bapaalde speler terug te geven op basis van id (path parameter). Net zoals de user-endpoint heeft deze een query parameter en heeft deze een token nodig.
![image](https://user-images.githubusercontent.com/57671114/211331067-fdd2ad60-a919-4a88-98bc-ddadcb48a9da.png)
