
class PlantScan:
     Tuple: Immutable reference for disease severity categories (Bonus Task)
    SEVERITY_LEVELS = ("Low", "Moderate", "Severe", "Critical")

     Class variable to track total scans across the system
    total_scans_performed = 0

    def __init__(self, scan_id: str, crop_name: str, symptoms: list):
        self.scan_id = scan_id
        self.crop_name = crop_name
        self.symptoms = symptoms
        self.diagnosis = "Pending Analysis"
        self.treatment = "None"
        self.severity = PlantScan.SEVERITY_LEVELS[0]
        
         Increment total scan counter
        PlantScan.total_scans_performed += 1

     Instance Method: Simulates diagnostic logic based on symptoms
    def run_diagnosis(self):
        symptom_set = set(s.lower() for s in self.symptoms)

        if "yellow leaves" in symptom_set or "stunted growth" in symptom_set:
            self.diagnosis = "Nitrogen Deficiency"
            self.treatment = "Apply nitrogen-rich organic compost or urea fertilizer."
            self.severity = PlantScan.SEVERITY_LEVELS[1] # Moderate
            
        elif "black spots" in symptom_set or "powdery mildew" in symptom_set:
            self.diagnosis = "Fungal Infection (Early Blight)"
            self.treatment = "Apply bio-fungicide and prune affected leaves."
            self.severity = PlantScan.SEVERITY_LEVELS[2] # Severe
            
        elif "wilting" in symptom_set or "root rot" in symptom_set:
            self.diagnosis = "Bacterial Wilt / Oversaturation"
            self.treatment = "Improve soil drainage and reduce irrigation frequency."
            self.severity = PlantScan.SEVERITY_LEVELS[3] # Critical
            
        else:
            self.diagnosis = "Healthy / Unknown Condition"
            self.treatment = "Continue routine watering and sunlight exposure."
            self.severity = PlantScan.SEVERITY_LEVELS[0] # Low

     Instance Method: Displays record details
    def display_scan_report(self):
        print(f"--- SCAN REPORT [{self.scan_id}] ---")
        print(f"Crop Type  : {self.crop_name}")
        print(f"Symptoms   : {', '.join(self.symptoms)}")
        print(f"Diagnosis  : {self.diagnosis}")
        print(f"Severity   : {self.severity}")
        print(f"Treatment  : {self.treatment}")
        print("-" * 35)

     Class Method (@classmethod): Returns system-wide total scan metrics
    @classmethod
    def get_total_scans(cls):
        return f"Total scans performed across system: {cls.total_scans_performed}"


class Farmer:
    def __init__(self, farmer_id: str, region: str):
         DPG Principle: Privacy-respecting (Stores non-identifying IDs & regions)
        self.farmer_id = farmer_id
        self.region = region
         Dictionary Data Structure: Stores scans with scan_id as key
        self.scans_records = {}

     Instance Method: Adds scan object to dictionary
    def add_scan(self, scan: PlantScan):
        scan.run_diagnosis()
        self.scans_records[scan.scan_id] = scan

     Instance Method: Display all records for this farmer
    def display_all_scans(self):
        print(f"\n==========================================")
        print(f"FARMER RECORD | ID: {self.farmer_id} | Region: {self.region}")
        print(f"==========================================")
        if not self.scans_records:
            print("No plant scans recorded.")
            return

        for scan_obj in self.scans_records.values():
            scan_obj.display_scan_report()


 ==========================================
 PROGRAM EXECUTION & INTERACTION
 ==========================================
if __name__ == "__main__":
     1. Instantiate Farmer (Anonymous ID for privacy)
    farmer_1 = Farmer(farmer_id="FARM-9021", region="Western Area")

     2. Instantiate PlantScan Objects
    scan_a = PlantScan(
        scan_id="SCN-001", 
        crop_name="Cassava", 
        symptoms=["yellow leaves", "stunted growth"]
    )
    
    scan_b = PlantScan(
        scan_id="SCN-002", 
        crop_name="Rice", 
        symptoms=["black spots", "powdery mildew"]
    )

     3. Add Scans to Farmer Record (Dictionary Storage)
    farmer_1.add_scan(scan_a)
    farmer_1.add_scan(scan_b)

     4. Display Outputs
    farmer_1.display_all_scans()

     5. Call Class Method
    print(PlantScan.get_total_scans())
