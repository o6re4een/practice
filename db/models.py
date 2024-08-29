from sqlalchemy import Column, Integer, String
from sqlalchemy import (
    LargeBinary,
    SmallInteger,
    Text,
    ForeignKey,
    DECIMAL,
    DateTime,
    CHAR,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gender(Base):
    __tablename__ = "gender"
    Gender = Column(String(1), primary_key=True)


class Country(Base):
    __tablename__ = "country"
    CountryCode = Column(CHAR(3), primary_key=True)
    CountryName = Column(String(100))
    CountryFlag = Column(LargeBinary)


class EventType(Base):
    __tablename__ = "eventtype"
    EventTypeId = Column(CHAR(2), primary_key=True)
    EventTypeName = Column(String(50))


class Marathon(Base):
    __tablename__ = "marathon"
    MarathonId = Column(Integer, primary_key=True)
    MarathonName = Column(String(80))
    CityName = Column(String(80))
    CountryCode = Column(CHAR(3), ForeignKey("country.CountryCode"))
    YearHeld = Column(SmallInteger)


class Event(Base):
    __tablename__ = "event"
    EventId = Column(CHAR(6), primary_key=True)
    EventName = Column(String(50))
    EventTypeId = Column(CHAR(2), ForeignKey("eventtype.EventTypeId"))
    MarathonId = Column(Integer, ForeignKey("marathon.MarathonId"))
    StartDateTime = Column(DateTime)
    Cost = Column(DECIMAL(10, 2))
    MaxParticipants = Column(SmallInteger)


class Charity(Base):
    __tablename__ = "charity"
    CharityId = Column(Integer, primary_key=True)
    CharityName = Column(String(100))
    CharityDescription = Column(String(200))
    CharityLogo = Column(String(50))


class User(Base):
    __tablename__ = "user"
    Email = Column(String(100), primary_key=True)
    Password = Column(String(100))
    FirstName = Column(String(80))
    LastName = Column(String(80))
    RoleId = Column(CHAR(1), ForeignKey("role.RoleId"))

    def __user_info__(self):
        return f"{self.FirstName} {self.LastName}"


class Role(Base):
    __tablename__ = "role"
    RoleId = Column(CHAR(1), primary_key=True)
    RoleName = Column(String(50))


class Volunteer(Base):
    __tablename__ = "volunteer"
    VolunteerId = Column(Integer, primary_key=True)
    FirstName = Column(String(80))
    LastName = Column(String(80))
    CountryCode = Column(CHAR(3), ForeignKey("country.CountryCode"))
    Gender = Column(String(10), ForeignKey("gender.Gender"))


class Timesheet(Base):
    __tablename__ = "timesheet"
    TimesheetNum = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    StartDate = Column(DateTime)
    EndDate = Column(DateTime)
    PaymentAmount = Column(DECIMAL(10, 2))


class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column(Integer, primary_key=True)
    FirstName = Column(Text)
    LastName = Column(Text)
    DateOfBirth = Column(DateTime)
    Gender = Column(String(1), ForeignKey("gender.Gender"))
    position_id = Column(Integer, ForeignKey("position.position_id"))
    EmailAddress = Column(Text)


class Position(Base):
    __tablename__ = "position"
    position_id = Column(Integer, primary_key=True)
    PositionName = Column(Text)
    PositionDescription = Column(Text)
    PayPeriod = Column(Text)
    PayRate = Column(Text)


class Runner(Base):
    __tablename__ = "runner"
    RunnerId = Column(Integer, primary_key=True)
    Email = Column(String(100))
    Gender = Column(String(10), ForeignKey("gender.Gender"))
    DateOfBirth = Column(DateTime)
    CountryCode = Column(CHAR(3), ForeignKey("country.CountryCode"))


class Registration(Base):
    __tablename__ = "registration"
    RegistrationId = Column(Integer, primary_key=True)
    RunnerId = Column(Integer, ForeignKey("runner.RunnerId"))
    RegistrationDateTime = Column(DateTime)
    RaceOptionId = Column(CHAR(1), ForeignKey("raceoption.RaceOptionId"))
    RegistrationStatusId = Column(
        Integer, ForeignKey("registrationstatus.RegistrationStatusId")
    )
    Cost = Column(DECIMAL(10, 2))
    SponsorshipTarget = Column(DECIMAL(10, 2))
    CharityId = Column(Integer, ForeignKey("charity.CharityId"))


class RegistrationEvent(Base):
    __tablename__ = "registrationevent"
    RegistrationEventId = Column(Integer, primary_key=True)
    RunnerId = Column(Integer, ForeignKey("runner.RunnerId"))
    EventId = Column(CHAR(6), ForeignKey("event.EventId"))
    BibNumber = Column(SmallInteger)
    RaceTime = Column(DECIMAL(10, 2))


class RaceOption(Base):
    __tablename__ = "raceoption"
    RaceOptionId = Column(CHAR(1), primary_key=True)
    RaceOptionName = Column(String(50))
    Cost = Column(DECIMAL(10, 2))


class RegistrationStatus(Base):
    __tablename__ = "registrationstatus"
    RegistrationStatusId = Column(SmallInteger, primary_key=True)
    RegistrationStatus = Column(String(80))


class Sponsorship(Base):
    __tablename__ = "sponsorship"
    SponsorshipId = Column(Integer, primary_key=True)
    SponsorName = Column(String(150))
    RegistrationId = Column(Integer, ForeignKey("registration.RegistrationId"))
    Amount = Column(DECIMAL(10, 2))
