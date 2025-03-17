from dataclasses import dataclass

@dataclass
class CursusData:
    id: int = None
    created_at: str = None
    name: str = None
    slug: str = None
    kind: str = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])

@dataclass
class VersionsData:
    large: str = None
    medium: str = None
    small: str = None
    micro: str = None
    
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])

@dataclass
class ProjectData:
    id: int = None
    name: str = None
    slug: str = None
    parent: str = None
    children: list = None
    attachments: list = None
    created_at: str = None
    updated_at: str = None
    exam: bool = None
    git_id: int = None
    repository: str = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])
@dataclass
class LanguageData:
    id: int = None
    name: str = None
    identifier: str = None
    created_at: str = None
    updated_at: str = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])

@dataclass
class CampusData:
    id: int = None
    name: str = None
    time_zone: str = None
    language: LanguageData = None
    users_count: int = None
    vogsphere_id: int = None
    country: str = None
    address: str = None
    zip: str = None
    city: str = None
    website: str = None
    facebook: str = None
    twitter: str = None
    active: bool = None
    email_extension: str = None
    default_hidden_phone: bool = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "language":
                setattr(self, key, LanguageData(data[key]))
            else:
                setattr(self, key, data[key])
@dataclass
class ExamData:
    id: int = None
    ip_range: str = None
    begin_at: str = None
    end_at: str = None
    location: str = None
    max_people: int = None
    nbr_subscribers: int = None
    name: str = None
    created_at: str = None
    updated_at: str = None
    campus: CampusData = None
    cursus: list[CursusData] = None
    projects: list[ProjectData] = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "campus":
                setattr(self, key, CampusData(data[key]))
            elif key == "cursus":
                cursus = []
                for i in data[key]:
                    cursus.append(CursusData(i))
                setattr(self, key, cursus)
            elif key == "projects":
                projects = []
                for i in data[key]:
                    projects.append(ProjectData(i))
                setattr(self, key, projects)
            else:
                setattr(self, key, data[key])


@dataclass
class ImageData:
    link: str = None
    versions: VersionsData = None
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "versions":
                setattr(self, key, VersionsData(data[key]))
            else:
                setattr(self, key, data[key])
@dataclass
class UserData:
    id: int = None
    email: str = None
    login: str = None
    first_name: str = None
    last_name: str = None
    usual_full_name: str = None
    usual_first_name: str = None
    url: str = None
    phone: str = None
    displayname: str = None
    kind: str = None
    image: ImageData = None
    staff: bool = None
    correction_point: int = None
    pool_month: str = None
    pool_year: str = None
    location: str = None
    wallet: int = None
    anonymize_date: str = None
    data_erasure_date: str = None
    created_at: str = None
    updated_at: str = None
    alumnized_at: str = None
    alumni: bool = None
    active: bool = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "image":
                setattr(self, key, ImageData(data[key]))
            else:
                setattr(self, key, data[key])

@dataclass
class CandidateData:
    id: int = None
    user_id: int = None
    birth_date: str = None
    gender: str = None
    zip_code: str = None 
    country: str = None
    birth_city: str = None
    birth_country: str = None
    postal_street: str = None
    postal_complement: str = None
    postal_city: str = None
    postal_zip_code: str = None 
    postal_country: str = None
    contact_affiliation: str = None
    contact_last_name: str = None
    contact_first_name: str = None
    contact_phone1: str = None
    contact_phone2: str = None
    max_level_memory: int = None
    max_level_logic: int = None 
    other_information: str = None
    language: str = None
    meeting_date: str = None
    piscine_date: str = None
    created_at: str = None
    updated_at: str = None
    phone: str = None
    email: str = None
    pin: str = None
    phone_country_code: str = None
    hidden_phone: bool = False
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])

@dataclass
class CursusUserData:
    id: int = None
    begin_at: str = None
    end_at: str = None
    grade: str = None
    level: float = None
    skills: list = None
    cursus_id: int = None
    has_coalition: bool = None
    blackholed_at: str = None
    created_at: str = None
    updated_at: str = None
    user: UserData = None
    cursus: CursusData = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "user":
                setattr(self, key, UserData(data[key]))
            elif key == "cursus":
                setattr(self, key, CursusData(data[key]))
            else:
                setattr(self, key, data[key])


@dataclass
class JournalData:
    id: int = None
    user_id: int = None
    cursus_id: int = None
    campus_id: int = None
    item_type: str = None
    item_id: int = None
    reason: str = None
    created_at: str = None
    updated_at: str = None
    event_at: str = None

    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])

@dataclass
class LocationData:
    id: int = None
    begin_at: str = None
    end_at: str = None
    primary: bool = None
    floor: str = None
    row: str = None
    post: str = None
    host: str = None
    campus_id: int = None
    user: UserData = None
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "user":
                setattr(self, key, UserData(data[key]))
            else:
                setattr(self, key, data[key])
    
@dataclass
class TransactionData:
    id: int = None
    user_id: int = None
    item_id: int = None
    item_type: str = None
    amount: int = None
    currency: str = None
    created_at: str = None
    updated_at: str = None
    kind: str = None
    status: str = None
    validated_at: str = None
    transaction_id: str = None
    data: str = None
    user: UserData = None
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "user":
                setattr(self, key, UserData(data[key]))
            else:
                setattr(self, key, data[key])

        
@dataclass
class AchivementData:
    id: int = None
    name: str = None
    description: str = None
    tier: str = None
    kind: str = None
    visible: bool = None
    image: str = None
    nbr_of_success: int = None
    users_url: str = None
    achievements: list = None
    parent: "AchivementData" = None
    title: str = None
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            if key == "parent":
                if data[key] is not None:
                    setattr(self, key, AchivementData(data[key]))
            else:
                setattr(self, key, data[key])

@dataclass
class AchivementUserData:
    id: int = None
    user_id: int = None
    login: str = None
    url: str = None
    created_at: str = None
    def __init__(self, data: dict = None):
        if data is None:
            raise ValueError("Data is required.")
        self.raw = data
        for key in data.keys():
            setattr(self, key, data[key])