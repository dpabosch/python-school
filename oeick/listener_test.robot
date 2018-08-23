*** Settings ***
Documentation    Zum Testen des Listener Interface

*** Test Cases ***
Listener_Interface_ausprobieren
    log    Zum Ausprobieren des Listeners
    ein keyword    Alpha    Beta    Gamma
    Breakpoint    Step
    noch ein keyword
    Ein Keyword das weitere Keywords aufruft, die wiederum Keywords aufrufen

Der zweite Test in dieser Suite
    #Breakpoint
    log    Es tut mir Leid, Dave, aber das kann ich nicht tun.
    Should be True    False

*** Keywords ***
ein keyword
    [Arguments]    ${erstes}    ${zweites}    ${drittes}
    log    ${erstes} ${zweites} ${drittes}

noch ein keyword
    log    ich bin noch ein keyword

Ein Keyword das weitere Keywords aufruft, die wiederum Keywords aufrufen
    Weiteres Keyword

Weiteres Keyword
    Wiederum ein Keyword

Wiederum ein Keyword
    Log    Bazinga!

Breakpoint
    [Arguments]    ${step}
    Log    Breakpoint