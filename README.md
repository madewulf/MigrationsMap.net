MigrationsMap.net
=================

This is the code of the site http://migrationsmap.net, including the scripts
used to generate the JSON data files.

* `parser.py` generates two Python matrices (in fact, dictionnaries of dictionnaries) from
  the file `global_migrant_origin_database_version_4.csv`: `matrix[country_code1][country_code2]`
  which allows to find the number of migrants leaving from country 1 to country 2 (countries
  are represented by their ISO 3166 three letters country code). `reversed_matrix` allows
  to find the number of migrants arriving, instead of leaving.
  In the processes of creating those matrices, two useful files are generated:
     * `code_to_name.json` a JSON object allowing to match iso country codes to country names
     * `name_to_code.json` allows the reverse translation from country names to country code

  `parser.py' also contains the function `geolocalize_the_world`
  which obtains geographic coordinates for every country of `code_to_name.json` from the Google
  geolocation api and stores it in `geoloc.json` (beware, because of some mistakes, this file
  has been manually edited after the process, for example because Georgia had been located
  in the U.S.A.).

The code is under MIT license. 


