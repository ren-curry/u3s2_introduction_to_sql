QRY_TOTAL_CHARACTERS = '''
                        SELECT COUNT(*)
                        FROM charactercreator_character
                       '''

QRY_TOTAL_SUBCLASSES = '''
                        SELECT 'Total Clerics', COUNT(*)
                        FROM charactercreator_character
                        INNER JOIN charactercreator_cleric
                        ON character_ptr_id = character_id

                        UNION ALL

                        SELECT 'Total Fighters', COUNT(*)
                        FROM charactercreator_character
                        INNER JOIN charactercreator_fighter
                        ON character_ptr_id = character_id

                        UNION ALL

                        SELECT 'Total Mages', COUNT(*)
                        FROM charactercreator_character
                        INNER JOIN charactercreator_mage
                        ON character_ptr_id = character_id

                        UNION ALL

                        SELECT 'Total Necromancers', COUNT(*)
                        FROM charactercreator_character
                        INNER JOIN charactercreator_mage
                        ON character_ptr_id = character_id
                        INNER JOIN charactercreator_necromancer
                        ON character_ptr_id = mage_ptr_id

                        UNION ALL

                        SELECT 'Total Thieves', COUNT(*)
                        FROM charactercreator_character
                        INNER JOIN charactercreator_thief
                        ON character_ptr_id = character_id
                       '''

QRY_TOTAL_ITEMS = '''
                    SELECT COUNT(*)
                    FROM  charactercreator_character_inventory
                  '''

QRY_ITEMS_WEAPONS_COUNT = '''
                            SELECT SUM(CASE WHEN item_ptr_id IS NULL THEN 1
                            ELSE 0 END)  AS 'Not Weapons', COUNT(item_ptr_id)
                            AS 'Weapons'
                            FROM  charactercreator_character_inventory ccci
                            INNER JOIN armory_item ai
                            ON ai.item_id = ccci.item_id
                            LEFT JOIN armory_weapon aw
                            ON aw.item_ptr_id = ai.item_id
                         '''

QRY_ITEMS_PER_CHARACTER = '''
                            SELECT ccc.name, COUNT(ccci.id)
                            FROM charactercreator_character ccc
                            LEFT JOIN charactercreator_character_inventory ccci
                            ON ccc.character_id = ccci.character_id
                            INNER JOIN armory_item ai
                            ON ai.item_id = ccci.item_id
                            AND aw.item_ptr_id IS NULL
                            LEFT JOIN armory_weapon aw
                            ON aw.item_ptr_id = ai.item_id
                            GROUP BY ccc.name
                            LIMIT 20
                          '''

QRY_WEAPONS_PER_CHARACTER = '''
                                SELECT ccc.name, COUNT(ccci.id)
                                FROM charactercreator_character ccc
                                LEFT JOIN
                                charactercreator_character_inventory ccci
                                ON ccc.character_id = ccci.character_id
                                INNER JOIN armory_item ai
                                ON ai.item_id = ccci.item_id
                                INNER JOIN armory_weapon aw
                                ON aw.item_ptr_id = ai.item_id
                                GROUP BY ccc.name
                                LIMIT 20
                            '''
