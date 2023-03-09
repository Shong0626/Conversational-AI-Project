def doesntKnowLeague():
    doesntKnowLeague = {
        'state':'doesntKnowLeague',
        '`That\'s fine. Do you play League of Legends?.`': {
            '[{yes, yeah}]':{
                'state':'familiarity',
                '`Who\'s your favorite champion?`':{
                    '[favorite champion]':{ #ontology for favorite champion
                        '`That champion is fun to play! This esports player plays them as well, and they\'re really fun to watch. I suggest watching them`':'end'
                    },
                    'error':'end'
                }
            },
            '[{no, not, dont}]':{
                'state':'explainLeague',
                '`That\'s fine. League is just an online 5 v 5 game, where players play champions that each have unique abilites, and the objective of the game is to kill the enemy player\'s nexus. Does that make sense?`':{
                    '[yes]': {
                        '`Nice! What got you interested in League?`':{
                            '[any response]':{
                                '`That\'s awesome! If you want to learn more, you should watch this player. He\'s pretty famous in the community, and I think it would be a good way to learn about the community.`':'end'
                            },
                            'error':'end'
                        }
                    },
                    '[no]':{
                        '`What are you confused about?`':'end' #explain more about league
                    },
                    'error':'end'
                }
            },
            'error':'doesntKnowLeague'
        }
    }
    return doesntKnowLeague