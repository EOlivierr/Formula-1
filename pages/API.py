import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import plotly.figure_factory as ff
import requests
import json

#url = "http://ergast.com/api/f1/driverStandings/1"
#response = requests.request("GET", url = url)
#json=response.json()
#API_data=pd.DataFrame(json)
<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet type="text/xsl" href="/schemas/mrd-1.5.xsl"?>
<MRData xmlns="http://ergast.com/mrd/1.5" series="f1" url="http://ergast.com/api/f1/driverstandings/1" limit="30" offset="0" total="72">
    <StandingsTable driverStandings="1">
        <StandingsList season="1950" round="7">
            <DriverStanding position="1" positionText="1" points="30" wins="3">
                <Driver driverId="farina" url="http://en.wikipedia.org/wiki/Nino_Farina">
                    <GivenName>Nino</GivenName>
                    <FamilyName>Farina</FamilyName>
                    <DateOfBirth>1906-10-30</DateOfBirth>
                    <Nationality>Italian</Nationality>
                </Driver>
                <Constructor constructorId="alfa" url="http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One">
                    <Name>Alfa Romeo</Name>
                    <Nationality>Swiss</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1951" round="8">
            <DriverStanding position="1" positionText="1" points="31" wins="3">
                <Driver driverId="fangio" url="http://en.wikipedia.org/wiki/Juan_Manuel_Fangio">
                    <GivenName>Juan</GivenName>
                    <FamilyName>Fangio</FamilyName>
                    <DateOfBirth>1911-06-24</DateOfBirth>
                    <Nationality>Argentine</Nationality>
                </Driver>
                <Constructor constructorId="alfa" url="http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One">
                    <Name>Alfa Romeo</Name>
                    <Nationality>Swiss</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1952" round="8">
            <DriverStanding position="1" positionText="1" points="36" wins="6">
                <Driver driverId="ascari" url="http://en.wikipedia.org/wiki/Alberto_Ascari">
                    <GivenName>Alberto</GivenName>
                    <FamilyName>Ascari</FamilyName>
                    <DateOfBirth>1918-07-13</DateOfBirth>
                    <Nationality>Italian</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1953" round="9">
            <DriverStanding position="1" positionText="1" points="34.5" wins="5">
                <Driver driverId="ascari" url="http://en.wikipedia.org/wiki/Alberto_Ascari">
                    <GivenName>Alberto</GivenName>
                    <FamilyName>Ascari</FamilyName>
                    <DateOfBirth>1918-07-13</DateOfBirth>
                    <Nationality>Italian</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1954" round="9">
            <DriverStanding position="1" positionText="1" points="42" wins="6">
                <Driver driverId="fangio" url="http://en.wikipedia.org/wiki/Juan_Manuel_Fangio">
                    <GivenName>Juan</GivenName>
                    <FamilyName>Fangio</FamilyName>
                    <DateOfBirth>1911-06-24</DateOfBirth>
                    <Nationality>Argentine</Nationality>
                </Driver>
                <Constructor constructorId="maserati" url="http://en.wikipedia.org/wiki/Maserati">
                    <Name>Maserati</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
                <Constructor constructorId="mercedes" url="http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One">
                    <Name>Mercedes</Name>
                    <Nationality>German</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1955" round="7">
            <DriverStanding position="1" positionText="1" points="40" wins="4">
                <Driver driverId="fangio" url="http://en.wikipedia.org/wiki/Juan_Manuel_Fangio">
                    <GivenName>Juan</GivenName>
                    <FamilyName>Fangio</FamilyName>
                    <DateOfBirth>1911-06-24</DateOfBirth>
                    <Nationality>Argentine</Nationality>
                </Driver>
                <Constructor constructorId="mercedes" url="http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One">
                    <Name>Mercedes</Name>
                    <Nationality>German</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1956" round="8">
            <DriverStanding position="1" positionText="1" points="30" wins="3">
                <Driver driverId="fangio" url="http://en.wikipedia.org/wiki/Juan_Manuel_Fangio">
                    <GivenName>Juan</GivenName>
                    <FamilyName>Fangio</FamilyName>
                    <DateOfBirth>1911-06-24</DateOfBirth>
                    <Nationality>Argentine</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1957" round="8">
            <DriverStanding position="1" positionText="1" points="40" wins="4">
                <Driver driverId="fangio" url="http://en.wikipedia.org/wiki/Juan_Manuel_Fangio">
                    <GivenName>Juan</GivenName>
                    <FamilyName>Fangio</FamilyName>
                    <DateOfBirth>1911-06-24</DateOfBirth>
                    <Nationality>Argentine</Nationality>
                </Driver>
                <Constructor constructorId="maserati" url="http://en.wikipedia.org/wiki/Maserati">
                    <Name>Maserati</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1958" round="11">
            <DriverStanding position="1" positionText="1" points="42" wins="1">
                <Driver driverId="hawthorn" url="http://en.wikipedia.org/wiki/Mike_Hawthorn">
                    <GivenName>Mike</GivenName>
                    <FamilyName>Hawthorn</FamilyName>
                    <DateOfBirth>1929-04-10</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1959" round="9">
            <DriverStanding position="1" positionText="1" points="31" wins="2">
                <Driver driverId="jack_brabham" url="http://en.wikipedia.org/wiki/Jack_Brabham">
                    <GivenName>Jack</GivenName>
                    <FamilyName>Brabham</FamilyName>
                    <DateOfBirth>1926-04-02</DateOfBirth>
                    <Nationality>Australian</Nationality>
                </Driver>
                <Constructor constructorId="cooper-climax" url="http://en.wikipedia.org/wiki/Cooper_Car_Company">
                    <Name>Cooper-Climax</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1960" round="10">
            <DriverStanding position="1" positionText="1" points="43" wins="5">
                <Driver driverId="jack_brabham" url="http://en.wikipedia.org/wiki/Jack_Brabham">
                    <GivenName>Jack</GivenName>
                    <FamilyName>Brabham</FamilyName>
                    <DateOfBirth>1926-04-02</DateOfBirth>
                    <Nationality>Australian</Nationality>
                </Driver>
                <Constructor constructorId="cooper-climax" url="http://en.wikipedia.org/wiki/Cooper_Car_Company">
                    <Name>Cooper-Climax</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1961" round="8">
            <DriverStanding position="1" positionText="1" points="34" wins="2">
                <Driver driverId="phil_hill" url="http://en.wikipedia.org/wiki/Phil_Hill">
                    <GivenName>Phil</GivenName>
                    <FamilyName>Hill</FamilyName>
                    <DateOfBirth>1927-04-20</DateOfBirth>
                    <Nationality>American</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1962" round="9">
            <DriverStanding position="1" positionText="1" points="42" wins="4">
                <Driver driverId="hill" url="http://en.wikipedia.org/wiki/Graham_Hill">
                    <GivenName>Graham</GivenName>
                    <FamilyName>Hill</FamilyName>
                    <DateOfBirth>1929-02-15</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="brm" url="http://en.wikipedia.org/wiki/BRM">
                    <Name>BRM</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1963" round="10">
            <DriverStanding position="1" positionText="1" points="54" wins="7">
                <Driver driverId="clark" url="http://en.wikipedia.org/wiki/Jim_Clark">
                    <GivenName>Jim</GivenName>
                    <FamilyName>Clark</FamilyName>
                    <DateOfBirth>1936-03-04</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="lotus-climax" url="http://en.wikipedia.org/wiki/Team_Lotus">
                    <Name>Lotus-Climax</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1964" round="10">
            <DriverStanding position="1" positionText="1" points="40" wins="2">
                <Driver driverId="surtees" url="http://en.wikipedia.org/wiki/John_Surtees">
                    <GivenName>John</GivenName>
                    <FamilyName>Surtees</FamilyName>
                    <DateOfBirth>1934-02-11</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1965" round="10">
            <DriverStanding position="1" positionText="1" points="54" wins="6">
                <Driver driverId="clark" url="http://en.wikipedia.org/wiki/Jim_Clark">
                    <GivenName>Jim</GivenName>
                    <FamilyName>Clark</FamilyName>
                    <DateOfBirth>1936-03-04</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="lotus-climax" url="http://en.wikipedia.org/wiki/Team_Lotus">
                    <Name>Lotus-Climax</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1966" round="9">
            <DriverStanding position="1" positionText="1" points="42" wins="4">
                <Driver driverId="jack_brabham" url="http://en.wikipedia.org/wiki/Jack_Brabham">
                    <GivenName>Jack</GivenName>
                    <FamilyName>Brabham</FamilyName>
                    <DateOfBirth>1926-04-02</DateOfBirth>
                    <Nationality>Australian</Nationality>
                </Driver>
                <Constructor constructorId="brabham-repco" url="http://en.wikipedia.org/wiki/Brabham">
                    <Name>Brabham-Repco</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1967" round="11">
            <DriverStanding position="1" positionText="1" points="51" wins="2">
                <Driver driverId="hulme" url="http://en.wikipedia.org/wiki/Denny_Hulme">
                    <GivenName>Denny</GivenName>
                    <FamilyName>Hulme</FamilyName>
                    <DateOfBirth>1936-06-18</DateOfBirth>
                    <Nationality>New Zealander</Nationality>
                </Driver>
                <Constructor constructorId="brabham-repco" url="http://en.wikipedia.org/wiki/Brabham">
                    <Name>Brabham-Repco</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1968" round="12">
            <DriverStanding position="1" positionText="1" points="48" wins="3">
                <Driver driverId="hill" url="http://en.wikipedia.org/wiki/Graham_Hill">
                    <GivenName>Graham</GivenName>
                    <FamilyName>Hill</FamilyName>
                    <DateOfBirth>1929-02-15</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="lotus-ford" url="http://en.wikipedia.org/wiki/Team_Lotus">
                    <Name>Lotus-Ford</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1969" round="11">
            <DriverStanding position="1" positionText="1" points="63" wins="6">
                <Driver driverId="stewart" url="http://en.wikipedia.org/wiki/Jackie_Stewart">
                    <GivenName>Jackie</GivenName>
                    <FamilyName>Stewart</FamilyName>
                    <DateOfBirth>1939-06-11</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="matra-ford" url="http://en.wikipedia.org/wiki/Matra">
                    <Name>Matra-Ford</Name>
                    <Nationality>French</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1970" round="13">
            <DriverStanding position="1" positionText="1" points="45" wins="5">
                <Driver driverId="rindt" url="http://en.wikipedia.org/wiki/Jochen_Rindt">
                    <GivenName>Jochen</GivenName>
                    <FamilyName>Rindt</FamilyName>
                    <DateOfBirth>1942-04-18</DateOfBirth>
                    <Nationality>Austrian</Nationality>
                </Driver>
                <Constructor constructorId="team_lotus" url="http://en.wikipedia.org/wiki/Team_Lotus">
                    <Name>Team Lotus</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1971" round="11">
            <DriverStanding position="1" positionText="1" points="62" wins="6">
                <Driver driverId="stewart" url="http://en.wikipedia.org/wiki/Jackie_Stewart">
                    <GivenName>Jackie</GivenName>
                    <FamilyName>Stewart</FamilyName>
                    <DateOfBirth>1939-06-11</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="tyrrell" url="http://en.wikipedia.org/wiki/Tyrrell_Racing">
                    <Name>Tyrrell</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1972" round="12">
            <DriverStanding position="1" positionText="1" points="61" wins="5">
                <Driver driverId="emerson_fittipaldi" url="http://en.wikipedia.org/wiki/Emerson_Fittipaldi">
                    <GivenName>Emerson</GivenName>
                    <FamilyName>Fittipaldi</FamilyName>
                    <DateOfBirth>1946-12-12</DateOfBirth>
                    <Nationality>Brazilian</Nationality>
                </Driver>
                <Constructor constructorId="team_lotus" url="http://en.wikipedia.org/wiki/Team_Lotus">
                    <Name>Team Lotus</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1973" round="15">
            <DriverStanding position="1" positionText="1" points="71" wins="5">
                <Driver driverId="stewart" url="http://en.wikipedia.org/wiki/Jackie_Stewart">
                    <GivenName>Jackie</GivenName>
                    <FamilyName>Stewart</FamilyName>
                    <DateOfBirth>1939-06-11</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="tyrrell" url="http://en.wikipedia.org/wiki/Tyrrell_Racing">
                    <Name>Tyrrell</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1974" round="15">
            <DriverStanding position="1" positionText="1" points="55" wins="3">
                <Driver driverId="emerson_fittipaldi" url="http://en.wikipedia.org/wiki/Emerson_Fittipaldi">
                    <GivenName>Emerson</GivenName>
                    <FamilyName>Fittipaldi</FamilyName>
                    <DateOfBirth>1946-12-12</DateOfBirth>
                    <Nationality>Brazilian</Nationality>
                </Driver>
                <Constructor constructorId="mclaren" url="http://en.wikipedia.org/wiki/McLaren">
                    <Name>McLaren</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1975" round="14">
            <DriverStanding position="1" positionText="1" points="64.5" wins="5">
                <Driver driverId="lauda" url="http://en.wikipedia.org/wiki/Niki_Lauda">
                    <GivenName>Niki</GivenName>
                    <FamilyName>Lauda</FamilyName>
                    <DateOfBirth>1949-02-22</DateOfBirth>
                    <Nationality>Austrian</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1976" round="16">
            <DriverStanding position="1" positionText="1" points="69" wins="6">
                <Driver driverId="hunt" url="http://en.wikipedia.org/wiki/James_Hunt">
                    <GivenName>James</GivenName>
                    <FamilyName>Hunt</FamilyName>
                    <DateOfBirth>1947-08-29</DateOfBirth>
                    <Nationality>British</Nationality>
                </Driver>
                <Constructor constructorId="mclaren" url="http://en.wikipedia.org/wiki/McLaren">
                    <Name>McLaren</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1977" round="17">
            <DriverStanding position="1" positionText="1" points="72" wins="3">
                <Driver driverId="lauda" url="http://en.wikipedia.org/wiki/Niki_Lauda">
                    <GivenName>Niki</GivenName>
                    <FamilyName>Lauda</FamilyName>
                    <DateOfBirth>1949-02-22</DateOfBirth>
                    <Nationality>Austrian</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1978" round="16">
            <DriverStanding position="1" positionText="1" points="64" wins="6">
                <Driver driverId="mario_andretti" url="http://en.wikipedia.org/wiki/Mario_Andretti">
                    <GivenName>Mario</GivenName>
                    <FamilyName>Andretti</FamilyName>
                    <DateOfBirth>1940-02-28</DateOfBirth>
                    <Nationality>American</Nationality>
                </Driver>
                <Constructor constructorId="team_lotus" url="http://en.wikipedia.org/wiki/Team_Lotus">
                    <Name>Team Lotus</Name>
                    <Nationality>British</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
        <StandingsList season="1979" round="15">
            <DriverStanding position="1" positionText="1" points="51" wins="3">
                <Driver driverId="scheckter" url="http://en.wikipedia.org/wiki/Jody_Scheckter">
                    <GivenName>Jody</GivenName>
                    <FamilyName>Scheckter</FamilyName>
                    <DateOfBirth>1950-01-29</DateOfBirth>
                    <Nationality>South African</Nationality>
                </Driver>
                <Constructor constructorId="ferrari" url="http://en.wikipedia.org/wiki/Scuderia_Ferrari">
                    <Name>Ferrari</Name>
                    <Nationality>Italian</Nationality>
                </Constructor>
            </DriverStanding>
        </StandingsList>
    </StandingsTable>
</MRData>

