# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2026 William Desportes <williamdes@wdes.fr>
# Copyright (C) 2018-2026 Isaac Bennetch
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# List of our sponsors
SPONSORS = {
    'diamond': [],
    'platinum': [],
    'gold': [
        { 'url': 'https://www.vapehuset.se/', 'logo': 'vapehuset.png', 'name': 'Vapehuset', 'sponsorList': 'skip'},
        { 'url': 'https://www.4kdownload.com/', 'logo': '4kdownload.png', 'name': '4K Download'},
        { 'url': 'https://vape.se/', 'logo': 'vape.png', 'name': 'Vape.se'},
        { 'url': 'https://superviral.io', 'logo': 'superviral.png', 'name': 'Superviral.io'},
        { 'url': 'https://www.ramotion.com/', 'logo': 'ramotion.png', 'name': 'Ramotion.com'},
        { 'url': 'https://unaimytext.com/', 'logo': 'unaimytext.png', 'name': 'UnAiMyText'},
        { 'url': 'https://socialboss.org/', 'logo': 'socialboss.png', 'name': 'SocialBoss'},
        { 'url': 'https://quickbookstoolhub.com/', 'logo': 'quickbookstoolhub.png', 'name': 'Quickbooks Tool Hub'},
        { 'url': 'https://buzzoid.com/', 'logo': 'buzzoid.png', 'name': 'Buy Instagram Followers & Likes'},
        { 'url': 'https://twicsy.com/', 'logo': 'twicsy.png', 'name': 'Buy Instagram Followers, Likes & Views'},
        { 'url': 'https://www.famety.net/', 'rel': 'sponsored', 'logo': 'famety.png', 'name': 'buy real Instagram followers from Famety'},
        { 'url': 'https://copycopter.ai/', 'logo': 'copycopter.png', 'name': 'CopyCopter.ai'},
        { 'url': 'https://www.idigic.net/', 'logo': 'idigic.png', 'name': 'Buy Instagram Followers, Likes & Views'},
        { 'url': 'https://buycheapestfollowers.com', 'logo': 'buycheapestfollowers.png', 'name': 'buycheapestfollowers.com'},
        { 'url': 'https://bountii.co', 'logo': 'bountii.png', 'name': 'bountii.co'},
        { 'url': 'https://celebian.com', 'logo': 'celebian.png', 'name': 'celebian.com'},
        { 'url': 'https://www.follower24.de/', 'logo': 'follower24.png', 'name': 'Buy followers, likes and views for Instagram and TikTok'},
        { 'url': 'https://viralyft.com/', 'logo': 'viralyft.png', 'name': 'Viralyft'},
        { 'url': 'https://www.socialboosting.com', 'logo': 'socialboosting.png', 'name': 'Social Boosting'},
        { 'url': 'https://www.vapes.se/', 'logo': 'vapes-se.png', 'name': 'Vapes.se'},
        { 'url': 'https://socialkings.online/', 'logo': 'socialkings.png', 'name': 'Socialkings'},
        { 'url': 'https://instant-famous.com', 'logo': 'instant_famous.png', 'name': 'Instant Famous'},
        { 'url': 'https://writehuman.ai/', 'logo': 'write_human.png', 'name': 'WriteHuman Humanize AI Text'},
        { 'url': 'https://freecrash.game/', 'logo': 'free_crash_game.png', 'name': 'Free to play multiplier game'},
        { 'url': 'https://www.socialwick.com', 'logo': 'socialwick.png', 'name': 'Social Wick'},

    ],
    'bronze': [
        { 'url': 'https://www.topbargains.com.au/', 'name': 'Australian Coupons'},
        { 'url': 'https://www.loadview-testing.com', 'name': 'Load View Testing'},
        { 'url': 'https://www.entertainment-nation.co.uk/', 'name': 'Entertainment Nation'},
        { 'url': 'https://www.gtxgaming.co.uk/', 'name': 'GTX Gaming'},
        { 'url': 'https://www.chefworks.com/', 'name': 'Chef Works Inc.'},
        { 'url': 'https://www.heerlaw.com', 'name': 'Heer Law'},
        { 'url': 'https://withcandour.co.uk', 'name': 'Candour Digital Agency'},
        { 'url': 'https://www.minitool.com', 'name': 'MiniTool'},
        { 'url': 'https://www.clfip.com', 'name': 'Chhabra Law Firm'},
        { 'url': 'https://www.milemarkmedia.com/', 'name': 'Legal Marketing'},
        { 'url': 'https://skepp.com/', 'name': 'SKEPP Office Rental'},
        { 'url': 'https://rabatkongen.dk', 'name': 'Rabatkongen rabatkoder'},
        { 'url': 'https://www.partitionwizard.com/', 'name': 'MiniTool Partition Wizard'},
        { 'url': 'https://comradeweb.com/', 'name': 'Comrade Digital Marketing Agency'},
        { 'url': 'https://www.lazarlaw.com', 'name': 'Austin Divorce Attorney'},
        { 'url': 'https://allelydbogapps.dk/', 'name': 'Lydbøger'},
        { 'url': 'https://www.prijsvergelijken.nl', 'name': 'prijsvergelijken.nl'},
        { 'url': 'https://www.autonomer.nl/', 'name': 'Autonomer'},
        { 'url': 'https://elavtaldirekt.se', 'name': 'Elavtaldirekt'},
        { 'url': 'https://webhostland.com/', 'name': 'Webhostland'},
        { 'url': 'https://dealspotr.com', 'name': 'Dealspotr Online Coupons'},
        { 'url': 'https://tryggvi.se', 'name': 'Tryggvi'},
        { 'url': 'https://cheatevolution.com', 'name': 'Cheat Evolution'},
        { 'url': 'https://americancardrooms.com', 'name': 'American Cardrooms'},
        { 'url': 'https://www.theory7.net', 'name': 'Theory7.net'},
        { 'url': 'https://goldstarsocial.com/', 'name': 'Goldstar Social'},
        { 'url': 'https://www.sveaiptv.com/', 'name': 'Bästa IPTV i Sverige'},
        { 'url': 'https://www.worthepenny.com/', 'name': 'WorthEPenny'},
        { 'url': 'https://www.easeus.com/', 'name': 'EaseUS Software'},
        { 'url': 'https://www.pinskylawoffice.ca', 'name': 'Calgary Business Lawyers'},
        { 'url': 'https://nodepositpromocodes.com', 'name': 'No Deposit Promo Codes'},
        { 'url': 'https://www.socialfollowers.uk', 'name': 'Social Followers'},
        { 'url': 'https://www.lambdatest.com', 'name': 'LambdaTest'},
        { 'url': 'https://iboysoft.com', 'name': 'iBoysoft'},
        { 'url': 'https://poprey.com', 'name': 'Poprey'},
        { 'url': 'https://earthweb.com', 'name': 'Earthweb'},
        { 'url': 'https://www.honrev.com', 'name': 'HONREV Honest Reviews'},
        { 'url': 'https://www.pmpmg.com/', 'name': 'Law Firm Marketing Services'},
        { 'url': 'https://tyres.co.uk/', 'name': 'Tyres.co.uk'},
    ],
}
