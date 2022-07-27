import kivy
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
import webbrowser

CalculatorActsCount = 0
CalculatorAdvantages = 0
CalculatorDisadvantages = 0
CalculatorBuff1 = 0
CalculatorBuff2 = 0
CalculatorBuff3 = 0
CalculatorDebuff1 = 0
CalculatorDebuff2 = 0
CalculatorDebuff3 = 0
CalculatorCheckDice = 0
CalculatorGate = 0
CalculatorResultCount = 0
CheckArray = ["0", "0", "0", "0"]
NewArray = ["0", "0", "0", "0"]

class MainApp(App):
    def on_start(self):
        self.InitializeUIClock = Clock.schedule_once(self.Reload, .5)
        pass

##############################################################################################################################
#UI
###########################
    def Reload(self, junk):
        #Wash screen
        self.root.ids.ScreenSlot.clear_widgets()
        pass
    def Pass(self):
        pass
    def ScreenSelect(self, ScreenName, LMButton1Text, LMButton2Text, LMButton3Text, LMButton4Text, LMButton5Text):
        #Trigger Reload(1)
        self.Reload(1)
        #Add widget specified in argument
        self.root.ids.ScreenSlot.add_widget(ScreenName)
        #Set lower menu buttons text, on_press and on_release attributes
        self.root.ids.LowerMenu1.text = LMButton1Text
        self.root.ids.LowerMenu2.text = LMButton2Text
        self.root.ids.LowerMenu3.text = LMButton3Text
        self.root.ids.LowerMenu4.text = LMButton4Text
        self.root.ids.LowerMenu5.text = LMButton5Text
        pass
    def BottomMenuButton(self, ButtonText):
        global CalculatorActsCount
        if ButtonText == "Check":
            self.MakeCheck()
        if ButtonText == "Clear Results":
            self.WipeResults()
        if ButtonText == "Clear Input":
            self.WipeInput()
        if ButtonText == f"Act: {CalculatorActsCount}":
            self.MakeAct()
        if ButtonText == "Clear Acts":
            self.WipeActsCount()
        if ButtonText == "Chron Calc":
            self.ScreenSelect(self.root.ids.ChronCalc, "Check", "Clear Results", "Clear Input", f"Act: {CalculatorActsCount}", "Clear Acts")
        if ButtonText == "Update":
            webbrowser.open("https://github.com/NotTheChargerYouNeeded/ChroniclesRPGSystem/raw/main/bin/ChronCalc-0.1-arm64-v8a_armeabi-v7a-debug.apk")
        pass
######################################################################################################################    























































##################################################################################################################################
#Main Calculator Application - User Interface
##################################################################################################################################
    def MakeAct(self):
        global CalculatorActsCount
        global CalculatorDisadvantages
        print("MakeAct Triggered")
        CalculatorDisadvantages = CalculatorDisadvantages + CalculatorActsCount
        self.MakeCheck()
        CalculatorActsCount += 1
        self.root.ids.LowerMenu4.text = f"Act: {CalculatorActsCount}"
    def MakeCheck(self):
        global CalculatorActsCount
        global CalculatorResultCount
        global CalculatorAdvantages
        global CalculatorDisadvantages
        global CalculatorBuff1
        global CalculatorBuff2
        global CalculatorBuff3
        global CalculatorDebuff1
        global CalculatorDebuff2
        global CalculatorDebuff3
        global CalculatorCheckDice
        global CalculatorResultCount
        print("MakeCheck Triggered")
        CalculatorResultCount += 1
        #Run Prep below here down to Content (Read In Input Variables)
        CalculatorAdvantages = int(self.root.ids.AdvantagesInput.text)
        CalculatorBuff1 = int(self.root.ids.BuffOneInput.text)
        if CalculatorBuff1 > 4:
            CalculatorBuff1 = 4
            self.root.ids.BuffOneInput.text = "4"
        CalculatorBuff2 = int(self.root.ids.BuffTwoInput.text)
        if CalculatorBuff2 > 4:
            CalculatorBuff2 = 4
            self.root.ids.BuffTwoInput.text = "4"
        CalculatorBuff3 = int(self.root.ids.BuffThreeInput.text)
        if CalculatorBuff3 > 4:
            CalculatorBuff3 = 4
            self.root.ids.BuffThreeInput.text = "4"
        CalculatorCheckDice = int(self.root.ids.CheckDiceInput.text)
        if CalculatorCheckDice > 4:
            CalculatorCheckDice = 4
            self.root.ids.CheckDiceInput.text = "4"
        CalculatorDebuff1 = int(self.root.ids.DebuffOneInput.text)
        if CalculatorDebuff1 > 4:
            CalculatorDebuff1 = 4
            self.root.ids.DebuffOneInput.text = "4"
        CalculatorDebuff2 = int(self.root.ids.DebuffTwoInput.text)
        if CalculatorDebuff2 > 4:
            CalculatorDebuff2 = 4
            self.root.ids.DebuffTwoInput.text = "4"
        CalculatorDebuff3 = int(self.root.ids.DebuffThreeInput.text)
        if CalculatorDebuff3 > 4:
            CalculatorDebuff3 = 4
            self.root.ids.DebuffThreeInput.text = "4"
        Temp = int(self.root.ids.DisadvantagesInput.text)
        CalculatorDisadvantages = CalculatorDisadvantages + Temp
        #Run Content below here
        print(f"Variable Contents Input To Brain: CalculatorAdvantages:{CalculatorAdvantages} | CalculatorDisadvantages:{CalculatorDisadvantages} | CalculatorBuff1:{CalculatorBuff1} | CalculatorBuff2:{CalculatorBuff2} | CalculatorBuff3:{CalculatorBuff3} | CalculatorDebuff1:{CalculatorDebuff1} | CalculatorDebuff2:{CalculatorDebuff2} | CalculatorDebuff3:{CalculatorDebuff3} | CalculatorCheckDice:{CalculatorCheckDice}")
        Brain(CalculatorAdvantages, CalculatorDisadvantages, CalculatorBuff1, CalculatorBuff2, CalculatorBuff3, CalculatorDebuff1, CalculatorDebuff2, CalculatorDebuff3, CalculatorCheckDice)
        CheckResultsOutput = f"Result {CalculatorResultCount}: |{CheckArray[0]}| |{CheckArray[1]}| |{CheckArray[2]}| |{CheckArray[3]}|"
        self.root.ids.ResultsGrid.add_widget(Label(size_hint=(1, .05), text=f"{CheckResultsOutput}"))
        #print( f"Result {CalculatorResultCount}: {CalculatorActsCount} | {CalculatorAdvantages} | {CalculatorDisadvantages} | {CalculatorBuff1} | {CalculatorBuff2} | {CalculatorBuff3} | {CalculatorDebuff1} | {CalculatorDebuff2} | {CalculatorDebuff3} | {CalculatorCheckDice}")
        #Run Content above here
        CalculatorAdvantages = 0
        CalculatorBuff1 = 0
        CalculatorBuff2 = 0
        CalculatorBuff3 = 0
        CalculatorCheckDice = 0
        CalculatorDebuff1 = 0
        CalculatorDebuff2 = 0
        CalculatorDebuff3 = 0
        CalculatorDisadvantages = 0
        #Run Prep above here up to Content (Clear Out Input Variable)

    def WipeInput(self):
        print("WipeInput Triggered")
        self.root.ids.AdvantagesInput.text = "0"
        self.root.ids.BuffOneInput.text = "0"
        self.root.ids.BuffTwoInput.text = "0"
        self.root.ids.BuffThreeInput.text = "0"
        self.root.ids.CheckDiceInput.text = "0"
        self.root.ids.DebuffOneInput.text = "0"
        self.root.ids.DebuffTwoInput.text = "0"
        self.root.ids.DebuffThreeInput.text = "0"
        self.root.ids.DisadvantagesInput.text = "0"
    def WipeResults(self):
        print("WipeResults Triggered")
        global CalculatorResultCount
        CalculatorResultCount = 0
        for child in [child for child in self.root.ids.ResultsGrid.children]:
            self.root.ids.ResultsGrid.remove_widget(child)
    def WipeActsCount(self):
        global CalculatorActsCount
        print("WipeActsCount Triggered")
        CalculatorActsCount = 0
        self.root.ids.LowerMenu4.text = f"Act: {CalculatorActsCount}"
##################################################################################################################################

























































###############################################################################################################################
#Main Calculator Application - Calculation Core
##############################################################################################################################################
import random
CheckArray = ["0", "0", "0", "0"]
NewArray = ["0", "0", "0", "0"]
def Brain(Advantages, Disadvantages, Buff1, Buff2, Buff3, Debuff1, Debuff2, Debuff3, CheckDice):
    print("Brain Triggered")
    Check_Array(CheckDice)
    if Buff1 > 0:
        print("Brain.Buff1 Triggered")
        Buff(CheckDice, Buff1)
        print("Brain.Buff1 Completed")
        pass
    if Debuff1 > 0:
        print("Brain.Debuff1 Triggered")
        Debuff(CheckDice, Debuff1)
        print("Brain.Debuff1 Completed")
        pass
    if Buff2 > 0:
        print("Brain.Buff2 Triggered")
        Buff(CheckDice, Buff2)
        print("Brain.Buff2 Completed")
        pass
    if Debuff2 > 0:
        print("Brain.Debuff2 Triggered")
        Debuff(CheckDice, Debuff2)
        print("Brain.Debuff2 Completed")
        pass
    if Buff3 > 0:
        print("Brain.Buff3 Triggered")
        Buff(CheckDice, Buff3)
        print("Brain.Buff3 Completed")
        pass
    if Debuff3 > 0:
        print("Brain.Debuff3 Triggered")
        Debuff(CheckDice, Debuff3)
        print("Brain.Debuff3 Completed")
        pass
    if Advantages > 0 and Advantages >= Disadvantages:
        print(f"Brain.AdvantagesCancel Triggered | (A){Advantages}:(D){Disadvantages}")
        Advantages = Advantages - Disadvantages
        Disadvantages = 0
        print(f"Brain.AdvantagesCancel Completed | (A){Advantages}:(D){Disadvantages}")
    if Disadvantages > 0 and Disadvantages >= Advantages:
        print(f"Brain.DisadvantagesCancel Triggered | (A){Advantages}:(D){Disadvantages}")
        Disadvantages = Disadvantages - Advantages
        Advantages = 0
        print(f"Brain.DisadvantagesCancel Completed | (A){Advantages}:(D){Disadvantages}")
    while Advantages > 0:
        AdvantagesFunction(CheckDice)
        Advantages -= 1
    while Disadvantages > 0:
        DisadvantagesFunction(CheckDice)
        Disadvantages -= 1

def Check_Array(Dice):
    print("Check_Array Triggered")
    CheckArray[0] = 0
    CheckArray[1] = 0
    CheckArray[2] = 0
    CheckArray[3] = 0
    if Dice == 1:
        CheckArray[0] = random.randint(1,6)
    if Dice == 2:
        CheckArray[0] = random.randint(1,6)
        CheckArray[1] = random.randint(1,6)
    if Dice == 3:
        CheckArray[0] = random.randint(1,6)
        CheckArray[1] = random.randint(1,6)
        CheckArray[2] = random.randint(1,6)
    if Dice == 4:
        CheckArray[0] = random.randint(1,6)
        CheckArray[1] = random.randint(1,6)
        CheckArray[2] = random.randint(1,6)
        CheckArray[3] = random.randint(1,6)
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")

def New_Array(Dice):
    print("New_Array Triggered")
    NewArray[0] = 0
    NewArray[1] = 0
    NewArray[2] = 0
    NewArray[3] = 0
    if Dice == 1:
        NewArray[0] = random.randint(1,6)
    if Dice == 2:
        NewArray[0] = random.randint(1,6)
        NewArray[1] = random.randint(1,6)
    if Dice == 3:
        NewArray[0] = random.randint(1,6)
        NewArray[1] = random.randint(1,6)
        NewArray[2] = random.randint(1,6)
    if Dice == 4:
        NewArray[0] = random.randint(1,6)
        NewArray[1] = random.randint(1,6)
        NewArray[2] = random.randint(1,6)
        NewArray[3] = random.randint(1,6)
    print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")

def FindHighestCheck(Dice):
    if CheckArray[0] == 0:
        return 0
    print("FindHighestCheck Triggered")
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
    if Dice == 1:
        Result = 1
    if Dice == 2:
        if CheckArray[0] >= CheckArray[1]:
            Result = 1
        if CheckArray[1] >= CheckArray[0]:
            Result = 2
    if Dice == 3:
        if CheckArray[0] >= CheckArray[1] and CheckArray[0] >= CheckArray[2]:
            Result = 1
        if CheckArray[1] >= CheckArray[0] and CheckArray[1] >= CheckArray[2]:
            Result = 2
        if CheckArray[2] >= CheckArray[0] and CheckArray[2] >= CheckArray[1]:
            Result = 3
    if Dice == 4:
        if CheckArray[0] >= CheckArray[1] and CheckArray[0] >= CheckArray[2] and CheckArray[0] >= CheckArray[3]:
            Result = 1
        if CheckArray[1] >= CheckArray[0] and CheckArray[1] >= CheckArray[2] and CheckArray[1] >= CheckArray[3]:
            Result = 2
        if CheckArray[2] >= CheckArray[0] and CheckArray[2] >= CheckArray[1] and CheckArray[2] >= CheckArray[3]:
            Result = 3
        if CheckArray[3] >= CheckArray[0] and CheckArray[3] >= CheckArray[1] and CheckArray[3] >= CheckArray[2]:
            Result = 4
    return Result

def FindHighestNew(Dice):
    if NewArray[0] == 0:
        return 0
    print("FindHighestNew Triggered")
    print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
    if Dice == 1:
        Result = 1
    if Dice == 2:
        if NewArray[0] >= NewArray[1]:
            Result = 1
        if NewArray[1] >= NewArray[0]:
            Result = 2
    if Dice == 3:
        if NewArray[0] >= NewArray[1] and NewArray[0] >= NewArray[2]:
            Result = 1
        if NewArray[1] >= NewArray[0] and NewArray[1] >= NewArray[2]:
            Result = 2
        if NewArray[2] >= NewArray[0] and NewArray[2] >= NewArray[1]:
            Result = 3
    if Dice == 4:
        if NewArray[0] >= NewArray[1] and NewArray[0] >= NewArray[2] and NewArray[0] >= NewArray[3]:
            Result = 1
        if NewArray[1] >= NewArray[0] and NewArray[1] >= NewArray[2] and NewArray[1] >= NewArray[3]:
            Result = 2
        if NewArray[2] >= NewArray[0] and NewArray[2] >= NewArray[1] and NewArray[2] >= NewArray[3]:
            Result = 3
        if NewArray[3] >= NewArray[0] and NewArray[3] >= NewArray[1] and NewArray[3] >= NewArray[2]:
            Result = 4
    return Result

def FindLowestCheck(Dice):
    if CheckArray[0] == 0:
        return 0
    print("FindLowestCheck Triggered")
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
    if Dice == 1:
        Result = 1
    if Dice == 2:
        if CheckArray[0] <= CheckArray[1]:
            Result = 1
        if CheckArray[1] <= CheckArray[0]:
            Result = 2
    if Dice == 3:
        if CheckArray[0] <= CheckArray[1] and CheckArray[0] <= CheckArray[2]:
            Result = 1
        if CheckArray[1] <= CheckArray[0] and CheckArray[1] <= CheckArray[2]:
            Result = 2
        if CheckArray[2] <= CheckArray[0] and CheckArray[2] <= CheckArray[1]:
            Result = 3
    if Dice == 4:
        if CheckArray[0] <= CheckArray[1] and CheckArray[0] <= CheckArray[2] and CheckArray[0] <= CheckArray[3]:
            Result = 1
        if CheckArray[1] <= CheckArray[0] and CheckArray[1] <= CheckArray[2] and CheckArray[1] <= CheckArray[3]:
            Result = 2
        if CheckArray[2] <= CheckArray[0] and CheckArray[2] <= CheckArray[1] and CheckArray[2] <= CheckArray[3]:
            Result = 3
        if CheckArray[3] <= CheckArray[0] and CheckArray[3] <= CheckArray[1] and CheckArray[3] <= CheckArray[2]:
            Result = 4
    return Result

def FindLowestNew(Dice):
    if NewArray[0] == 0:
        return 0
    print("FindLowestNew Triggered")
    print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
    if Dice == 1:
        Result = 1
    if Dice == 2:
        if NewArray[0] <= NewArray[1]:
            Result = 1
        if NewArray[1] <= NewArray[0]:
            Result = 2
    if Dice == 3:
        if NewArray[0] <= NewArray[1] and NewArray[0] <= NewArray[2]:
            Result = 1
        if NewArray[1] <= NewArray[0] and NewArray[1] <= NewArray[2]:
            Result = 2
        if NewArray[2] <= NewArray[0] and NewArray[2] <= NewArray[1]:
            Result = 3
    if Dice == 4:
        if NewArray[0] <= NewArray[1] and NewArray[0] <= NewArray[2] and NewArray[0] <= NewArray[3]:
            Result = 1
        if NewArray[1] <= NewArray[0] and NewArray[1] <= NewArray[2] and NewArray[1] <= NewArray[3]:
            Result = 2
        if NewArray[2] <= NewArray[0] and NewArray[2] <= NewArray[1] and NewArray[2] <= NewArray[3]:
            Result = 3
        if NewArray[3] <= NewArray[0] and NewArray[3] <= NewArray[1] and NewArray[3] <= NewArray[2]:
            Result = 4
    return Result

def AdvantagesFunction(CDice):
    print("Advantages Triggered")
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
    New_Array(1)
    LowestCheckDie = FindLowestCheck(CDice)
    if LowestCheckDie == 1 and CheckArray[0] < 6:
        while NewArray[0] <= CheckArray[0]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[0] = NewArray[0]
    if LowestCheckDie == 2 and CheckArray[1] < 6:
        while NewArray[0] <= CheckArray[1]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[1] = NewArray[0]
    if LowestCheckDie == 3 and CheckArray[2] < 6:
        while NewArray[0] <= CheckArray[2]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[2] = NewArray[0]
    if LowestCheckDie == 4 and CheckArray[3] < 6:
        while NewArray[0] <= CheckArray[3]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[3] = NewArray[0]
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
        
def DisadvantagesFunction(CDice):
    print("Disadvantages Triggered")
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
    New_Array(1)
    HighestCheckDie = FindHighestCheck(CDice)
    if HighestCheckDie == 1 and CheckArray[0] > 1:
        while NewArray[0] >= CheckArray[0]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[0] = NewArray[0]
    if HighestCheckDie == 2 and CheckArray[1] > 1:
        while NewArray[0] >= CheckArray[1]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[1] = NewArray[0]
    if HighestCheckDie == 3 and CheckArray[2] > 1:
        while NewArray[0] >= CheckArray[2]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[2] = NewArray[0]
    if HighestCheckDie == 4 and CheckArray[3] > 1:
        while NewArray[0] >= CheckArray[3]:
            NewArray[0] = random.randint(1,6)
            print(f"Non-Check Dice: {NewArray[0]} | {NewArray[1]} | {NewArray[2]} | {NewArray[3]}")
        CheckArray[3] = NewArray[0]
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")

def Buff(CDice, Dice):
    if Dice == 0:
        return
    print("Buff Triggered")
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
    New_Array(Dice)
    HighestNewDie = FindHighestNew(Dice)
    LowestCheckDie = FindLowestCheck(CDice)
    if CDice == 4 and Dice == 4:
        if LowestCheckDie == 4 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[3]:
                CheckArray[3] = NewArray[3]
        if LowestCheckDie == 4 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[3]:
                CheckArray[3] = NewArray[2]
        if LowestCheckDie == 4 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[3]:
                CheckArray[3] = NewArray[1]
        if LowestCheckDie == 4 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if LowestCheckDie == 3 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[2]:
                CheckArray[2] = NewArray[3]
        if LowestCheckDie == 3 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if LowestCheckDie == 3 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[1]:
                CheckArray[1] = NewArray[3]
        if LowestCheckDie == 2 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[0]:
                CheckArray[0] = NewArray[3]
        if LowestCheckDie == 1 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]
            
    if CDice == 4 and Dice == 3:
        if LowestCheckDie == 4 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[3]:
                CheckArray[3] = NewArray[2]
        if LowestCheckDie == 4 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[3]:
                CheckArray[3] = NewArray[1]
        if LowestCheckDie == 4 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if LowestCheckDie == 3 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if LowestCheckDie == 3 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 4 and Dice == 2:
        if LowestCheckDie == 4 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[3]:
                CheckArray[3] = NewArray[1]
        if LowestCheckDie == 4 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if LowestCheckDie == 3 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 4 and Dice == 1:
        if LowestCheckDie == 4 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 4:
        if LowestCheckDie == 3 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[2]:
                CheckArray[2] = NewArray[3]
        if LowestCheckDie == 3 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if LowestCheckDie == 3 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[1]:
                CheckArray[1] = NewArray[3]
        if LowestCheckDie == 2 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[0]:
                CheckArray[0] = NewArray[3]
        if LowestCheckDie == 1 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 3:
        if LowestCheckDie == 3 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if LowestCheckDie == 3 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 2:
        if LowestCheckDie == 3 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 1:
        if LowestCheckDie == 3 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 4:
        if LowestCheckDie == 2 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[1]:
                CheckArray[1] = NewArray[3]
        if LowestCheckDie == 2 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 4:
            if NewArray[3] > CheckArray[0]:
                CheckArray[0] = NewArray[3]
        if LowestCheckDie == 1 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 3:
        if LowestCheckDie == 2 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 3:
            if NewArray[2] > CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 2:
        if LowestCheckDie == 2 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 2:
            if NewArray[1] > CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 1:
        if LowestCheckDie == 2 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if LowestCheckDie == 1 and HighestNewDie == 1:
            if NewArray[0] > CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 1 and Dice == 4:
        if HighestNewDie == 4 and NewArray[3] > CheckArray[0]:
            CheckArray[0] = NewArray[3]
        if HighestNewDie == 3 and NewArray[2] > CheckArray[0]:
            CheckArray[0] = NewArray[2]
        if HighestNewDie == 2 and NewArray[1] > CheckArray[0]:
            CheckArray[0] = NewArray[1]
        if HighestNewDie == 1 and NewArray[0] > CheckArray[0]:
            CheckArray[0] = NewArray[0]
    if CDice == 1 and Dice == 3:
        if HighestNewDie == 3 and NewArray[2] > CheckArray[0]:
            CheckArray[0] = NewArray[2]
        if HighestNewDie == 2 and NewArray[1] > CheckArray[0]:
            CheckArray[0] = NewArray[1]
        if HighestNewDie == 1 and NewArray[0] > CheckArray[0]:
            CheckArray[0] = NewArray[0]
    if CDice == 1 and Dice == 2:
        if HighestNewDie == 2 and NewArray[1] > CheckArray[0]:
            CheckArray[0] = NewArray[1]
        if HighestNewDie == 1 and NewArray[0] > CheckArray[0]:
            CheckArray[0] = NewArray[0]
    if CDice == 1 and Dice == 1:
        if HighestNewDie == 1 and NewArray[0] > CheckArray[0]:
            CheckArray[0] = NewArray[0]
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")

def Debuff(CDice, Dice):
    if Dice == 0:
        return
    print("Debuff Triggered")
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
    New_Array(Dice)
    LowestNewDie = FindLowestNew(Dice)
    HighestCheckDie = FindHighestCheck(CDice)
    if CDice == 4 and Dice == 4:
        if HighestCheckDie == 4 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[3]:
                CheckArray[3] = NewArray[3]
        if HighestCheckDie == 4 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[3]:
                CheckArray[3] = NewArray[2]
        if HighestCheckDie == 4 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[3]:
                CheckArray[3] = NewArray[1]
        if HighestCheckDie == 4 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if HighestCheckDie == 3 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[2]:
                CheckArray[2] = NewArray[3]
        if HighestCheckDie == 3 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if HighestCheckDie == 3 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[1]:
                CheckArray[1] = NewArray[3]
        if HighestCheckDie == 2 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[0]:
                CheckArray[0] = NewArray[3]
        if HighestCheckDie == 1 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]
            
    if CDice == 4 and Dice == 3:
        if HighestCheckDie == 4 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[3]:
                CheckArray[3] = NewArray[2]
        if HighestCheckDie == 4 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[3]:
                CheckArray[3] = NewArray[1]
        if HighestCheckDie == 4 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if HighestCheckDie == 3 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if HighestCheckDie == 3 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 4 and Dice == 2:
        if HighestCheckDie == 4 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[3]:
                CheckArray[3] = NewArray[1]
        if HighestCheckDie == 4 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if HighestCheckDie == 3 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 4 and Dice == 1:
        if HighestCheckDie == 4 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[3]:
                CheckArray[3] = NewArray[0]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 4:
        if HighestCheckDie == 3 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[2]:
                CheckArray[2] = NewArray[3]
        if HighestCheckDie == 3 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if HighestCheckDie == 3 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[1]:
                CheckArray[1] = NewArray[3]
        if HighestCheckDie == 2 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[0]:
                CheckArray[0] = NewArray[3]
        if HighestCheckDie == 1 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 3:
        if HighestCheckDie == 3 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[2]:
                CheckArray[2] = NewArray[2]
        if HighestCheckDie == 3 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 2:
        if HighestCheckDie == 3 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[2]:
                CheckArray[2] = NewArray[1]
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 3 and Dice == 1:
        if HighestCheckDie == 3 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[2]:
                CheckArray[2] = NewArray[0]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 4:
        if HighestCheckDie == 2 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[1]:
                CheckArray[1] = NewArray[3]
        if HighestCheckDie == 2 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 4:
            if NewArray[3] < CheckArray[0]:
                CheckArray[0] = NewArray[3]
        if HighestCheckDie == 1 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 3:
        if HighestCheckDie == 2 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[1]:
                CheckArray[1] = NewArray[2]
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 3:
            if NewArray[2] < CheckArray[0]:
                CheckArray[0] = NewArray[2]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 2:
        if HighestCheckDie == 2 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[1]:
                CheckArray[1] = NewArray[1]
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 2:
            if NewArray[1] < CheckArray[0]:
                CheckArray[0] = NewArray[1]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 2 and Dice == 1:
        if HighestCheckDie == 2 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[1]:
                CheckArray[1] = NewArray[0]
        if HighestCheckDie == 1 and LowestNewDie == 1:
            if NewArray[0] < CheckArray[0]:
                CheckArray[0] = NewArray[0]

    if CDice == 1 and Dice == 4:
        if LowestNewDie == 4 and NewArray[3] < CheckArray[0]:
            CheckArray[0] = NewArray[3]
        if LowestNewDie == 3 and NewArray[2] < CheckArray[0]:
            CheckArray[0] = NewArray[2]
        if LowestNewDie == 2 and NewArray[1] < CheckArray[0]:
            CheckArray[0] = NewArray[1]
        if LowestNewDie == 1 and NewArray[0] < CheckArray[0]:
            CheckArray[0] = NewArray[0]
    if CDice == 1 and Dice == 3:
        if LowestNewDie == 3 and NewArray[2] < CheckArray[0]:
            CheckArray[0] = NewArray[2]
        if LowestNewDie == 2 and NewArray[1] < CheckArray[0]:
            CheckArray[0] = NewArray[1]
        if LowestNewDie == 1 and NewArray[0] < CheckArray[0]:
            CheckArray[0] = NewArray[0]
    if CDice == 1 and Dice == 2:
        if LowestNewDie == 2 and NewArray[1] < CheckArray[0]:
            CheckArray[0] = NewArray[1]
        if LowestNewDie == 1 and NewArray[0] < CheckArray[0]:
            CheckArray[0] = NewArray[0]
    if CDice == 1 and Dice == 1:
        if LowestNewDie == 1 and NewArray[0] < CheckArray[0]:
            CheckArray[0] = NewArray[0]
    print(f"Current: {CheckArray[0]} | {CheckArray[1]} | {CheckArray[2]} | {CheckArray[3]}")
##################################################################################################################################

























MainApp().run()
