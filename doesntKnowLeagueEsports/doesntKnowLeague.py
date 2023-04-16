from .IntroduceLeague import IntroduceLeague
from .laneInfo import laneInfo

IntroduceLeague = IntroduceLeague()
laneInfo = laneInfo()

def doesntKnowLeague():
    doesntKnowLeague = {
        'state': 'doesntKnowLeagueEsports',
        '`Have you ever played League of Legends?`': {
            'state': 'playedLOL',
            '[{yes, yeah, yup}]': {
                'state': 'familiarity',
                '`Who\'s your favorite champion?`': {
                    '#UserChamp': {
                        # ontology for favorite champion. Does not unfortunately handle cases where user has no favorite champion
                        '$FAV_CHAMP `is fun to play!` $PLAYER_RECOMMEND`plays them as well.`': 'end'
                    },
                    '[{dont, no, not}]': {
                        '`All good. My favorite champion is Irelia. I like playing aggressively and getting kills, so I find playing Irelia pretty fun.`': 'end'
                    },
                    'error': 'end'
                }
            },
            # TODO: add new branch here
            '[{heard, [video game]}]': {
                '`Yeah, it\'s actually one of the most popular video games in the world! It\'s a competitive, team-based game that\'s played by millions of people, and it has a thriving e-sports scene. Would you like to learn more about the game or the esports scene?`': {
                    '[{game, learn}]': 'IntroduceGame',
                    '[{esports, scene}]': 'IntroduceEsports',
                    'error': 'IntroduceGame'
                }
            },
            '[{no, nope, not, dont, never, barely, little bit}]': {
                'state': 'transit',
                # Casual questions to collect related infos
                # TODO: rewrite the casual converstaion part to add depth and smooth transitions
                '#GATE `What\'s your favorite game?`': {
                    'score': '0.8',
                    # TODO: catch circumstance if the user do not have favorite game
                    '[#FAV_GAMETYPE]': {
                        '`I love` #GET_FAV_GAME `too !` #GET_REASON_FAV_GAME `. `': 'transit'
                    },
                    'error': {
                        '`Cool`': 'transit'
                    }
                },

                '#GATE `May I know why are you interested in knowing more about League esports?`': {
                    'score': '1.0',
                    'state': 'interest',
                    '[{friend, friends, social, community}]': {
                        '`Yeah, a shared interest in games connects friends together. What do you typically do with friends in your free time?`': {
                            '[#ACTIVITY_WITH_FRIENDS]': {
                                '`Definitely, I wish I would have the chance to` #GET_ACTIVITY_FRIEND `with my friends too.`': 'transit'
                            },
                        }
                    },
                    '[{fun,challenging, exciting}]': {
                        '`For sure! After all, the adrenaline rush after watching an exciting matches is true. Do you enjoy the watching other sports events as well?`': {
                            '[#SportEvents]': {
                                # TODO to add different attitude toward different games
                                '`(^ρ^)/, Wow,I love` #GET_SportsEvent `too. My emotion get quickly driven by the players, and I love that feeling !`': {
                                    '[{too, [as well]}, yeah, sure, true]': {
                                        'score': '0.5',
                                        '`Hmm, I don\'t know where the excitement exactly come from, but I did feel connected when I watched the sport event, even it\'s online. `': {

                                            '[{yeah,well,true,too}]': {
                                                '`What do you think of esport event then`': {
                                                    '[{#ESportAttitudeChecker}]': {
                                                        '`#ESportAttitudeResponse`': {
                                                            # TODO: complete the branch

                                                        }

                                                    },

                                                }

                                            },
                                            'error': {
                                                '`Cool, in this case what do you think about the esport event of virtual games?`': 'esportAttitude',
                                            }

                                        }
                                    }
                                },

                                'error': {
                                    '`Cool, in this case what do you think about the esports event of virtual games?`': {
                                        'state': 'esportAttitude',
                                    }
                                }

                            }
                        }
                    },

                    '[{waste, time}]': {
                        '`Ha, sounds like you\'ve fallen into the trap of modernism. I guess there are better ways to use your time.`': 'transit'
                    },

                    '[$FAV_PLAYER=#ONT(leagues)]': {
                        '#IF($FAV_PLAYER = jojopyun) `Agree! Jojopyun is my favorite player too.`': 'transit',
                        '`I like` $FAV_PLAYER `too`': 'transit',
                        'error': 'loveLeague',
                    },
                    '[{not, not really, no, dont, nothing}]': {
                        '`Oh ok, so I guess you just want to get some info on the subject.`': 'transit'
                    },
                    '[{bye, exit}]': {
                        'state': 'quit',
                        '`Adieu, hope to see you again.`': 'end'
                    },
                    'error': {
                        'state': 'loveLeague',
                        '`Cool, I also love to watch league e-sports with friends. The exciting performance of the '
                        'players always fascinates me`': 'transit'
                    },
                },

                '`Let me give you a brief introduction to League of Legends. is actually one of the most popular video games in the world! It\'s a competitive, team-based game played by millions of people, and it has a thriving e-sports scene. Do you want to know more about the game or its e-sports scene?`': {
                    'score': '0.5',
                    '[{game, learn}]': 'IntroduceGame',
                    '[{esports, scene}]': 'IntroduceEsports',
                    'error': 'IntroduceGame'
                }

            },

            'error': {
                '`Sorry, I didn\'t catch that, could you say it again? ξ( ✿＞◡❛)`': 'playedLOL'
            },

        },

    }

    IntroduceGame = {
        'state': 'IntroduceGame',
        '`In League of Legends, there are five main roles: Top, Jungle, Mid, AD Carry, and Support. Each role has specific responsibilities and champion types. Damage dealers focus on dealing damage to enemy champions, tanks absorb damage and protect their teammates, and supports provide utility to their team through healing, crowd control, and vision control. The map is divided into three lanes and a jungle area. Players must work together, communicate, and strategize to secure objectives and outplay their opponents. What would you like to know more about: the different types of champions, in-game objectives, or the roles in the game?`': {
            '[{champions, types}]': 'IntroduceChampions',
            '[{objectives, in-game}]': 'IntroduceObjectives',
            '[{roles, positions}]': 'IntroduceRoles',
            '[{lane, lanes}]': 'laneInfo',
            '[{map, layout}]': 'IntroduceMap',
            '[{no, nothing, fine}]': 'EndIntroduceGame',
            'error': {
                'state': 'IntroduceGameRepeat',
                '`I\'m sorry, I didn\'t quite understand your question. Would you like to know more about the different types of champions, in-game objectives, roles in the game, or the map layout?`': {
                    '[{champions, types}]': 'IntroduceChampions',
                    '[{objectives, in-game}]': 'IntroduceObjectives',
                    '[{roles, positions, lanes}]': 'IntroduceRoles',
                    '[{map, layout}]': 'IntroduceMap',
                    '[{no, nothing, fine}]': 'EndIntroduceGame',
                    'error': 'IntroduceChampions'
                }
            }
        }
    }

    IntroduceChampions = {
        'state': 'IntroduceChampions',
        '`League of Legends has over 150 unique champions, each with their own abilities and playstyle! It\'s so diverse and exciting. (ゝ∀･)b`': {
            'state': 'InnerIntroduceChampions',
            '[{specific, champions}]': 'SpecificChampions',
            '[{roles, team}]': 'ChampionRoles',
            '[{types, categories}]': 'ChampionTypes',
            '[{popular, favorite}]': 'PopularChampions',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you have any questions about champions, feel free to ask!`': 'InnerIntroduceChampions'
            }
        }
    }

    SpecificChampions = {
        'state': 'SpecificChampions',
        '`For beginners, I recommend trying Garen (a strong fighter), Ashe (a skilled marksman), and Lux (a powerful mage). These champs have straightforward mechanics, so it\'s easier for new players to learn the ropes.(っ＾▿＾)っ Interested in more champ suggestions for each role?`': {
            'state': 'InnerSpecificChamp',
            '[{yes, sure, recommend}]': 'RecommendChampions',
            '[{no, not now, later}]': {
                'state': 'EndSpecificChampions',
                '`No worries! If you ever have questions about champions or anything else related to League of Legends, just ask anytime. Enjoy exploring the game! (ゝ∀･)b`': 'end'
            },
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you have any questions about champions, feel free to ask!`': 'InnerSpecificChampions'
            }
        }
    }

    ChampionTypes = {
        'state': 'ChampionTypes',
        '`Champions are grouped into six main classes: assassins, fighters, mages, marksmen, supports, and tanks. Each class offers a unique playstyle. Is there a specific class you\'d like to know more about?`': {
            'state': 'InnerChampionTypes',
            '[{assassins}]': {
                'state': 'AssassinsInfo',
                '`Assassins are like ninjas - fast, sneaky, and deadly! They excel at picking off high-value targets. Popular assassins include Zed, Katarina, and Fizz. Feel free to ask about other champion types or anything else about the game!`': {
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': 'AssassinsInfo'
                }
            },
            '[{fighters}]': {
                'state': 'FightersInfo',
                '`Fighters are like brawlers - strong and resilient! They excel in close combat and can take a beating while dishing out damage. Popular fighters include Darius, Garen, and Illaoi. Feel free to ask about other champion types or anything else about the game!`': {
                    'state': 'InnerFighters',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                        '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerFighters'
                    }
                }
            },
            '[{mages}]': {
                'state': 'MagesInfo',
                '`Mages are the spellcasters of the game, wielding powerful magic to obliterate their enemies. Popular mages include Lux, Veigar, and Annie. Curious about other champion types or any other aspect of the game? Just ask!`': {
                    'state': 'InnerMage',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerMage',
                    }
                }
            },
            '[{marksmen}]': {
                'state': 'MarksmenInfo',
                '`Marksmen are the sharpshooters of the game, dealing consistent damage from a distance. Popular marksmen include Ashe, Miss Fortune, and Jhin. Feel free to ask about other champion types or anything else about the game!`': {
                    'state': 'InnerMarksmen',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerMarksmen'
                    }
                }
            },
            '[{supports}]': {
                'state': 'SupportsInfo',
                '`Supports are the unsung heroes of the game, providing utility, protection, and vision for their team. Popular supports include Soraka, Thresh, and Lulu. Feel free to ask about other champion types or anything else about the game!`': {
                    'state': 'InnerSupports',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerSupports'
                    }
                }
            },
            '[{tanks}]': {
                'state': 'TanksInfo',
                '`Tanks are the juggernauts of the game, soaking up damage and protecting their allies. Popular tanks include Malphite, Ornn, and Sion. Feel free to ask about other champion types or anything else about the game!`': {
                    'state':'InnerTanks',
                    '[{other types, champion types}]': 'ChampionTypes',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    'error': {
                         '`(≧∀≦)ゞ I\'m really sorry, I didn\'t catch that. Could you explain what you\'re asking again?`': 'InnerTanks'
                    }
                }
            },
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerChampionTypes'
            }
        }
    }

    PopularChampions = {
        'state': 'PopularChampions',
        '`Some popular champions among players include Ahri, Yasuo, and Lux. They all have unique abilities that make them stand out. Do you want to know more about any specific champion?`': {
            '[{Ahri}]': {
                'state': 'AhriInfo',
                '`Ahri is a charming mage-assassin. With her quick dashes and mesmerizing abilities, she can leave enemies dazed and confused. Think you might want to give her a try? Or maybe learn about other champions?`': {
                    'state': 'InnerAhri',
                    '[{yes, try, play}]': {
                        'state': 'GiveAhriTry',
                        # TODO
                        '`Great! Have fun mastering Ahri\'s abilities and charming your way to victory! Remember, practice makes perfect. If you have any questions or want to learn about other aspects of the game, just let me know!`': 'end'
                    },
                    '[{other champions, more champions}]': 'PopularChampions',
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerAhri',
                    }
                }
            },
            '[{Yasuo}]': {
                'state': 'YasuoInfo',
                '`Yasuo is a skilled swordsman who can cut through enemies like a whirlwind! His high mobility and damage make him a thrilling champion to play. Interested in giving him a shot or exploring other champions?`': {
                    'state': 'InnerYasuo',
                    '[{yes, try, play}]': {
                        'state': 'GiveYasuoTry',
                        '`Awesome! Enjoy mastering Yasuo\'s swift moves and sharp skills. Just like Yasuo, stay focused and you\'ll soon become a force to be reckoned with! If you need help or want to learn more about the game, I\'m here to help!`': 'end'
                    },
                    '[{other champions, more champions}]': 'PopularChampions',
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerYasuo',
                    }
                }
            },
            '[{Lux}]': {
                'state': 'LuxInfo',
                '`Lux is a light-wielding mage who brightens up the battlefield! Her abilities include a snare, an area-of-effect damage spell, a shield, and a long-range laser for her ultimate. She\'s not just great at dealing damage but also has utility to support her team. Do you want to know about other champions, or maybe ask about roles, objectives, or anything else related to League of Legends?`': {
                    'state': 'InnerLux',
                    '[{other champions, champions}]': 'PopularChampions',
                    '[{roles}]': 'ChampionRoles',
                    '[{objectives}]': 'IntroduceObjectives',
                    '[{champion types, types}]': 'ChampionTypes',
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about a specific class, just let me know!`': 'InnerLux'
                    }
                }
            },
            '[{another, other}]': 'AnotherChampion',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about the champions, just let me know!`': 'InnerChampionTypes'
            }
        }
    }

    RecommendChampions = {
        'state': 'RecommendChampions',
        '`Here\' s a list of easy - to - learn champions for each role: 🌟Top: Garen, Malphite, Darius - Jungle: Warwick, Amumu, Vi - Mid: Annie, Lux, Veigar - ADC: Ashe, Miss Fortune, Sivir - Support: Soraka, Leona, Morgana.Try them out and find the ones that fit your playstyle best! ε(*´･∀･｀)зﾞReady to learn about the in -game objectives?`': {
            '[{yes, objectives, sure}]': 'IntroduceObjectives',
            '[{no, not now, later}]': 'EndObjectives',
            'error': 'IntroduceObjectives'
        }
    }

    ChampionRoles = {
        'state': 'ChampionRoles',
        'In a team, champions play specific roles based on their strengths and abilities. The roles are Top, Jungle, Mid, ADC, and Support. Each role contributes to the overall success of the team. Which role sounds interesting to you?': {
            'state': 'InnerChampionRole',
            '[{top}]': {
                'state': 'TopInfo',
                'Top lane is usually home to tanky fighters or bruisers. They tend to have high survivability and often engage in duels with their lane opponents. It\'s an exciting role if you enjoy 1v1 combat. What other roles intrigue you?': {
                    '[{jungle, mid, adc, support}]': 'InnerChampionRole',
                    'error': 'InnerChampionRole'
                }
            },

            '[{jungle}]': {
                'state': 'JungleInfo',
                '`Junglers roam the map, farming neutral monsters and helping teammates by ganking lanes. They play a pivotal role in securing objectives and controlling the map. It\'s a great role if you enjoy being a playmaker. Are you curious about other roles?`': {
                    '[{top, mid, adc, support}]': 'InnerChampionRole',
                    'error': 'InnerChampionRole'
                }
            },

            '[{mid}]': {
                'state': 'MidInfo',
                '`Mid laners are often mages or assassins with strong burst damage and crowd control. They have a big impact on the game, and their ability to roam and help other lanes is crucial. If you like dealing lots of damage and making plays, this role is for you. Interested in other roles?`': {
                    '[{top, jungle, adc, support}]': 'InnerChampionRole',
                    'error': 'InnerChampionRole'
                }
            },

            '[{adc}]': {
                'state': 'ADCInfo',
                '`ADCs, or Attack Damage Carries, are ranged champions that deal consistent physical damage. Their main goal is to dish out damage while staying safe in team fights. If you enjoy positioning and kiting, this role is perfect for you. Want to learn about other roles?`': {
                    '[{top, jungle, mid, support}]': 'InnerChampionRole',
                    'error': 'InnerChampionRole'
                }
            },

            '[{support}]': {
                'state': 'SupportInfo',
                '`Supports protect their team and provide utility through healing, crowd control, and vision control. They are the backbone of the team and help set up plays. If you like helping your teammates and controlling the game, this role is for you. Curious about other roles?`': {
                    '[{top, jungle, mid, adc}]': 'InnerChampionRole',
                    'error': 'InnerChampionRole'
                }
            },

            '[{esport, esports}]': 'IntroduceEsports',

            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about the different champions roles, just let me know!`': 'InnerChampionRole'
            }
        }
    }

    IntroduceObjectives = {
        'state': 'IntroduceObjectives',
        '`In-game objectives are crucial to winning in League of Legends. The main objectives are turrets, inhibitors, dragons, the Rift Herald, Baron Nashor, and the enemy Nexus. Turrets and inhibitors defend each team\'s base, while dragons and the Rift Herald grant powerful buffs to the team that defeats them.Baron Nashor grants a powerful buff to the entire team, helping them push lanes and destroy the enemy base. Ultimately, the goal is to destroy the enemy Nexus. Would you like to know more about the esports scene or are you ready to try the game?`': {
            '[{turrets}]': 'TurretsInfo',
            '[{dragons}]': 'DragonsInfo',
            '[{Baron, Nashor}]': 'BaronInfo',
            '[{esports, scene}]': 'IntroduceEsports',
            '[{try, game}]': 'ReadyToTry',
            'error': 'IntroduceEsports'

        }
    }

    IntroduceEsports = {
        'state': 'IntroduceEsports',
        '`League of Legends esports is a highly competitive scene with regional and international tournaments. The most prestigious event is the League of Legends World Championship, where the best teams from around the world compete for the title of world champion. Regional leagues, like the LCS (North America), LEC (Europe), LPL (China), and LCK (Korea), have regular seasons and playoffs that lead to international events. Top players can earn fame, fortune, and the adoration of fans. Would you like to learn more about specific teams or players?`': {
            '[{teams, specific}]': 'SpecificTeams',
            '[{players, specific}]': 'SpecificPlayers',
            '[{game, works}]': 'IntroduceChampions',
            '[{professional, teams}]': {
                'state': 'ProTeamsInfo',
                '`In the LoL e-sports scene, teams usually have coaches, analysts, and support staff to help them prepare for matches. They practice together, work on strategies, and scout their opponents to find weaknesses they can exploit. Most regions have their own professional leagues, like the LEC in Europe, LCS in North America, and LCK in Korea. Are you interested in major international competitions or how teams qualify for them?`': {
                    'state': 'InnerProTeams',
                    '[{international, competitions}]': {
                        'state': 'InternationalCompetitions',
                        '`The two biggest international events are the Mid-Season Invitational (MSI) and the League of Legends World Championship, or just Worlds. MSI happens around the middle of the year, while Worlds takes place in the fall. Would you like to learn more about how teams qualify for these events or how players make a living from e-sports?`': {
                            'state': 'InnerInternationalCompetitions',
                            '[{qualify, events}]': 'QualifyCompetitions',
                            '[{living, esports}]': 'EsportsLiving',
                            'error': {
                                '`I\'m sorry, I didn\'t catch that. If you want to know more about how teams qualify for events or how players make a living from e-sports, just let me know!`': 'InnerInternationalCompetitions',
                            }
                        }
                    },
                    '[{how, qualify}]': {
                        'state': 'QualifyCompetitions',
                        '`Teams earn championship points throughout the year based on their performance in regional leagues and the MSI. The teams with the most points at the end of the season qualify for Worlds, with additional spots awarded through regional playoffs and a last-chance qualifier. Are you curious about the financial aspect of e-sports or how to start watching LoL e-sports?`': {
                            'state': 'InnerQualification',
                            '[{financial, aspect}]': {
                                'state': 'EsportsLiving',
                                '`Many pro LoL players make a good living from salaries, sponsorships, and prize money. Some of the top players are even considered celebrities in their home countries. The e-sports industry is growing rapidly, and there are more opportunities than ever for talented players. Are you interested in watching e-sports games on streaming platforms or how to get into playing the game?`': {
                                    'state': 'InnerEsportLiving',
                                    '[{watching, streaming}]': {
                                        'state': 'StreamingPlatforms',
                                        '`Streaming platforms like Twitch and YouTube are essential for the growth and popularity of e-sports. Fans can watch live matches, replays, and highlights, as well as follow their favorite players and teams. Some pro players even stream their own gameplay and interact with fans during their downtime. Do you want to know how to start watching League of Legends e-sports or how to start playing the game yourself?`': {
                                            'state': 'InnerStreamingPlatforms',
                                            '[{watch, watching}]': 'StartWatching',
                                            '[{play, playing}]': 'StartPlaying',
                                            'error': {
                                                '`I\'m sorry, I didn\'t catch that. If you want to know more about how to start watching League of Legends e-sports or how to start playing the game, just let me know!`': 'InnerStreamingPlatforms'
                                            }
                                        }
                                    },
                                    '[{playing, game}]': 'StartPlaying',
                                    'error': {
                                        '`I\'m sorry, I didn\'t catch that. If you want to know more about watching e-sports on streaming platforms or how to get into playing the game, just let me know!`': 'InnerEsportLiving'
                                    }
                                }
                            },
                            '[{watching, esports}]': 'StartWatching',
                            'error': {
                                '`I\'m sorry, I didn\'t catch that. If you want to know more about the financial aspect of e-sports or how to start watching LoL e-sports, just let me know!`': 'InnerQualification',
                            }
                        }
                    },
                    'error': {
                        '`I\'m sorry, I didn\'t catch that. If you want to know more about international competitions or how teams qualify for them, just let me know!`': 'InnerProTeams',
                    }
                }
            },
            '[{no, not now, later}]': {
                'state': 'EndEsports',
                '`That\'s totally fine! If you ever want to learn more about the esports scene or anything else related to League of Legends, feel free to ask.Have a great time playing the game!`': 'end'
            },
            'error': 'SpecificTeams'
        }
    }

    SpecificTeams = {
        'state': 'SpecificTeams',
        '`Some of the most famous and successful teams in League of Legends history include T1 (formerly SK Telecom T1) from Korea, Fnatic and G2 Esports from Europe, and Team SoloMid and Cloud9 from North America. These teams have consistently performed well in their regional leagues and at international events. Are you interested in learning about specific players?`': {
            '[{yes, players, specific}]': 'SpecificPlayers',
            '[{no, not now, later}]': {
                'state': 'EndPlayers',
                '`Okay! If you ever want to know more about specific players or anything else related to League of Legends, just let me know. Enjoy your journey into the world of League of Legends!`': 'end'
            },
            'error': 'SpecificPlayers'
        }
    }

    SpecificPlayers = {
        'state': 'SpecificPlayers',
        '`Some legendary players in the history of League of Legends esports are Faker (mid laner for T1), Uzi (former ADC for Royal Never Give Up), Caps (mid laner for G2 Esports), and Doublelift (former ADC for Team SoloMid and Team Liquid). These players have had successful careers and have made a significant impact on the esports scene. I hope this information has been helpful. Are you ready to try the game now?`': {
            '[{yes, try, game}]': {
                'state': 'ReadyToTry',
                # TODO not lead to end
                '`Great! You can download League of Legends for free from the official website. It\'s available on Windows and macOS.I hope you have fun exploring the game and finding your favorite champions.If you have any more questions, don\'t hesitate to ask!`': 'end'
            },
            '[{no, not now, later}]': {
                'state': 'EndReadyToTry',
                '`No worries! If you ever decide to give League of Legends a try, or if you have any more questions, feel free to ask. Have a great day!`': 'end'
            },
            'error': 'ReadyToTry'
        }
    }

    StartWatching = {
        'state': 'StartWatching',
        '`I\'d recommend starting with the regional leagues, like the LEC, LCS, or LCK. This will give you a good introduction to the teams and players, as well as the overall competitive landscape. From there, you can move on to international events like MSI and Worlds. If you\'re interested in playing the game, it\'s free and there are plenty of resources available to help you learn!`': {
            'state': 'InnerStartWatching',
            '[{playing, game}]': 'StartPlaying',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about playing the game, just let me know!`': 'InnerStartWatching',
            }
        }
    }

    StartPlaying = {
        'state': 'StartPlaying',
        '`While there is a learning curve, the game is free to play, and there are plenty of resources available to help you learn. You can find guides, tutorials, and community forums online to help you improve your skills. Plus, playing with friends can make the experience more enjoyable. If you ever have any questions or want to play together, just let me know!`': {
            'state': 'InnerStartPlaying',
            'error': {
                '`I\'m sorry, I didn\'t catch that. If you want to know more about playing the game or anything else related to League of Legends, just let me know!`': 'InnerStartPlaying'
            }
        }
    }

    items = {
        'state': 'items',
        '`Items are intimidating at first glance, but they\'re actually pretty simple. Items are purchased from the '
        'store in your base, and they provide positive effects to you. Most items provide stat bonuses, but some grant '
        'a passive ability, and some are consumables that have some effect when used. Do you want me to explain any '
        'of that in more depth?`': {
            '[{how}, {buy}, {money, gold}]': {
                '`Items are bought with gold, which you passively acquire throughout the game. You can also get more '
                'gold by defeating minions, enemy champs, or jungle monsters, or by destroying enemy structures. Any '
                'other item questions?`': {
                    '[{-think, no, nope}]': {
                        '`Great, any other general League questions?`': 'IntroduceLeague'
                    },
                    'error': 'items'
                }
            }
        }
        # TODO: add info about items
    }

    base = {
        'state': 'base',
        '`Each team has their base at opposite corners of the map. The base is where players respawn after getting '
        'killed, as well as where they can heal their HP and buy items. The nexus is in the center of the base, '
        'protected by 2 turrets which do massive damage to champions in their range. Once one team destroys their '
        'opponents nexus, they win the game.`': 'end'
    }

    return doesntKnowLeague, items, base, laneInfo, IntroduceLeague, IntroduceGame, IntroduceChampions, IntroduceEsports, IntroduceObjectives, ChampionRoles, SpecificTeams, SpecificChampions, SpecificPlayers, RecommendChampions, PopularChampions, ChampionTypes,ChampionRoles, StartPlaying, StartWatching
