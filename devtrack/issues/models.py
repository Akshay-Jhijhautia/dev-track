from django.db import models

# Create your models here.
from abc import ABC, abstractmethod
from datetime import datetime

class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }

class Reporter(BaseEntity):
    def __init__(self,id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team
    
    def validate(self):
        if not isinstance(self.id, int):
            raise ValueError("Reporter Id must be an integer")
        
        if not self.name:
            raise ValueError("Name cannot be empty")
        
        if not self.email or '@' not in self.email:
            raise ValueError("Invalid email")
        
        if not self.team:
            raise ValueError("Team cannot be empty")
    
class Issue(BaseEntity):
    ALLOWED_STATUSES = ["open", "in_progress", "resolved", "closed"]
    ALLOWED_PRIORITIES = ["low", "medium", "high", "critical"]

    def __init__(self, id, title, description, status, priority, reporter_id, created_at = None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = created_at or str(datetime.now())
    
    def validate(self):
        if not isinstance(self.id, int):
            raise ValueError("Issue id must be an integer")
        
        if not self.title:
            raise ValueError("Title cannot be empty")
        
        if self.status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status")
        
        if self.priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Invalid Priority")
        
        if not isinstance(self.reporter_id, int):
            raise ValueError("Reporter Id must be an Integer")
    
    def describe(self):
        return f"{self.title} [{self.priority}]"

class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT] {self.title}"

class LowPriotityIssue(Issue):
    def describe(self):
        return f"{self.title}"

