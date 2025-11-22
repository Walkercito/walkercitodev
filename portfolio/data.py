import json
from pydantic import BaseModel
from typing import Any
import requests
import time
import os

BOT_TOKEN = 'MTIwODE2MjU1ODM4NTg1MjQyNg.GqVIBR.74HgSYq9S5VzOQvUdIuuNAXRg-olZmp0RsidrE'
USER_ID = '457318022357712906'
AVATAR_UPDATE_INTERVAL = 604800  # 1 week in seconds


class Media(BaseModel):
    email: str
    cv: str
    kofi: str = ""
    github: str
    linkedin: str
    twitter: str
    telegram: str
    discord: str = ""


class Tech(BaseModel):
    icon: str
    name: str


class Info(BaseModel):
    icon: str
    title: str
    subtitle: str
    description: str
    date: str = ""
    certificate: str = ""
    technologies: list["Tech"] = []
    image: str = ""
    url: str = ""
    github: str = ""


class Extra(BaseModel):
    image: str
    title: str
    description: str
    url: str


class Donations(BaseModel):
    title: str
    description: str
    value: str
    icon: str
    color: str


class Data(BaseModel):
    title: str
    description: str
    image: str
    avatar: str
    name: str
    skill: str
    location: str
    media: Media
    about: Any
    technologies: list[Tech]
    experience: list[Info]
    projects: list[Info]
    training: list[Info]
    extras: list[Extra]
    donations: list[Donations]

def get_discord_avatar():
    url = f'https://discord.com/api/v10/users/{USER_ID}'
    headers = {
        'Authorization': f'Bot {BOT_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        avatar_hash = user_data.get('avatar')
        user_id = user_data.get('id')
        
        if avatar_hash:
            avatar_extension = 'gif' if avatar_hash.startswith('a_') else 'png'
            return f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.{avatar_extension}'
    
    return None

def update_avatar_if_needed(data):
    avatar_path = 'assets/avatar.jpg'
    
    if os.path.exists(avatar_path):
        last_modified = os.path.getmtime(avatar_path)
        if time.time() - last_modified < AVATAR_UPDATE_INTERVAL:
            return
    
    new_avatar_url = get_discord_avatar()
    if new_avatar_url:
        response = requests.get(new_avatar_url)
        if response.status_code == 200:
            with open(avatar_path, 'wb') as f:
                f.write(response.content)
            data.avatar = avatar_path

with open("assets/data/data.json") as file:
    json_data = json.load(file)

if 'technologies' in json_data:
    json_data['technologies'] = [Tech(**tech) for tech in json_data['technologies']]
if 'experience' in json_data:
    json_data['experience'] = [Info(**info) for info in json_data['experience']]
if 'projects' in json_data:
    json_data['projects'] = [Info(**info) for info in json_data['projects']]
if 'training' in json_data:
    json_data['training'] = [Info(**info) for info in json_data['training']]
if 'extras' in json_data:
    json_data['extras'] = [Extra(**extra) for extra in json_data['extras']]
if 'media' in json_data:
    json_data['media'] = Media(**json_data['media'])
if "donations" in json_data:
    json_data['donations'] = [Donations(**donation) for donation in json_data['donations']]

data = Data(**json_data)
update_avatar_if_needed(data)