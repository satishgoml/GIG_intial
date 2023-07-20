from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'user_info'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    place = Column('place', String)
    phone = Column('phone', String, nullable=False)
    email = Column('email', String, nullable=False)
    hashed_password = Column('hashed_password', String, nullable=False)
    created_on_date = Column('created_on', DateTime, default=func.now(), nullable=False)
    updated_on_date = Column('updated_on', DateTime, default=func.now(), nullable=False)


class Designation(Base):
    __tablename__ = 'designation'
    id = Column('id', Integer, primary_key=True)
    designation_name = Column('designation_name', String, nullable=False)
    description = Column('description', String)


class Skill(Base):
    __tablename__ = 'skill'
    id = Column('id', Integer, primary_key=True)
    skill_name = Column('skill_name', String, nullable=False)
    description = Column('description', String)


class UserCareerInfo(Base):
    __tablename__ = 'user_career_info'
    id = Column('id', Integer, primary_key=True)
    designation_id = Column('designation_id', Integer, ForeignKey('designation.id'))
    experience_in_yrs = Column('experience_in_yrs', Integer, nullable=False)
    experience_in_months = Column('experience_in_months', Integer, nullable=False)
    additional_skills = Column('additional_skills', String)
    price_per_hour = Column('price_per_hour', String)
    work_type = Column('work_type', String)
    cv = Column('cv', String)
    user_info_id = Column('user_info_id', Integer, ForeignKey('user_info.id'))
    created_on = Column('created_on', DateTime, default=func.now(), nullable=False)
    updated_on = Column('updated_on', DateTime, default=func.now(), nullable=False)


class UserSkillSet(Base):
    __tablename__ = 'user_skill_set'

    id = Column('id', Integer, primary_key=True)
    skill_id = Column('skill_id', Integer, ForeignKey('skill.id'))
    yrs_of_experience = Column('yrs_of_experience', Integer, nullable=False)
    user_career_info_id = Column('user_career_info_id', Integer, ForeignKey('user_career_info.id'))
    created_on = Column('created_on', DateTime, default=func.now(), nullable=False)
    updated_on = Column('updated_on', DateTime, default=func.now(), nullable=False)
