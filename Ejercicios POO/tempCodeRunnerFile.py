import json
from datetime import datetime

class Persona:
    def __init__(self,nombre,edad,genero):
        
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        
    def __str__(self):
        
       return f"{self.nombre},{self.edad} años,{self.genero}"

class Diagnostico:
    
    def __init__(self,sintomas,diagnostico,tratamiento):

        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.tratamiento=tratamiento

    def __str__(self):
        
        return f"[{self.fecha}] Sintomas: {self.sintomas} | Diagnostico: {self.diagnostico} | Tratamiento: {self.tratamiento}"
    
    def to_dict(self):
        return {
            "fecha": self.fecha,
            "sintomas": self.sintomas,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento
        }

class Paciente (Persona):
    def __init__(self, nombre, edad, genero,id_paciente):
        super().__init__(nombre, edad, genero)
        self.id_paciente=id_paciente
        self.historial=[]
        self.citas=[]
    
    def agregar_diagnostico(self,diagnostico: Diagnostico):
        
        self.historial.append(diagnostico)
        
    def agendar_cita(self,medico,fecha_hora):
        self.citas.append(Cita(medico,fecha_hora))
        
    def mostrar_historial(self):
        for historial in self.historial:
            print(historial)
            
    def to_dict(self):
        return {
            "id_paciente": self.id_paciente,
            "nombre": self.nombre,
            "edad": self.edad,
            "genero": self.genero,
            "historial": [d.to_dict() for d in self.historial],
            "citas": [c.to_dict() for c in self.citas]
        }


class Medico (Persona):
    def __init__(self, nombre, edad, genero,id_medico,especialidad):
        super().__init__(nombre, edad, genero)
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.especialidad=especialidad
        self.id_medico=id_medico
        self.pacientes=[]
        self.citas=[]

    def diagnosticar(self,paciente:Paciente,sintomas,diagnostico,tratamiento):
        
        miDiagnostico=Diagnostico(sintomas,diagnostico,tratamiento)
        paciente.agregar_diagnostico(miDiagnostico)
        self.agregar_paciente(paciente)
        
    
    def agregar_paciente(self,paciente:Paciente):
        
        self.pacientes.append(paciente)
        
    def __str__(self):
        return super().__str__()+f"ID: {self.id_medico} | Especilidad: {self.especialidad}\n"
    
    def to_dict(self):
        return {
            "id_medico": self.id_medico,
            "nombre": self.nombre,
            "edad": self.edad,
            "genero": self.genero,
            "especialidad": self.especialidad,
            "pacientes": [p.id_paciente for p in self.pacientes],
            "citas": [c.to_dict() for c in self.citas]
        }
    



class Cita:
    def __init__(self,medico:Medico,fecha_hora):
        
        self.medico=medico
        self.fecha_hora=fecha_hora
        
    def to_dict(self):
        
        return {"Medico":self.medico.id_medico,
                "Fecha_hora":self.fecha_hora}

class Hospital:
    def __init__(self):
        self.pacientes=[]
        self.medicos=[]
    
    def agregar_paciente(self,paciente:Paciente):
        self.pacientes.append(paciente)
    
    def agregar_medico(self,medico:Medico):
        self.medicos.append(medico)
    
    def buscar_paciente(self,id_paciente)->Paciente:
        return next((p for p in self.pacientes if p.id_paciente==id_paciente),None)
    
    def buscar_medico(self,id_medico)->Medico:
        return next((m for m in self.medicos if m.id_medico==id_medico),None)
    
    def mostrar_todo(self):
        print(f"\n====== Pacientes ========\n")
        for p in self.pacientes:
            print(p)
        print(f"\n====== Medicos ========\n")
        for m in self.medicos:
            print(m)
        print("============================")
            
    # ----- Citas -----
    def agendar_cita(self, id_paciente, id_medico, fecha_hora):
        paciente = self.buscar_paciente(id_paciente)
        medico = self.buscar_medico(id_medico)
        if paciente and medico:
            paciente.agendar_cita(medico, fecha_hora)
            print(f"Cita agendada para {paciente.nombre} con {medico.nombre} el {fecha_hora}")
        else:
            print("Paciente o médico no encontrado.")

    # ----- Estadísticas -----
    def estadisticas(self):
        print("\n--- Estadísticas del Hospital ---")
        # Pacientes por especialidad
        espec_dict = {}
        for medico in self.medicos:
            espec_dict[medico.especialidad] = espec_dict.get(medico.especialidad, 0) + len(medico.pacientes)
        print("Pacientes por especialidad:", espec_dict)

        # Diagnósticos más comunes
        diag_count = {}
        for paciente in self.pacientes:
            for diag in paciente.historial:
                diag_count[diag.diagnostico] = diag_count.get(diag.diagnostico, 0) + 1
        print("Diagnósticos más comunes:", diag_count)

    # ----- Persistencia -----
    def guardar_datos(self, archivo="hospital.json"):
        data = {
            "pacientes": [p.to_dict() for p in self.pacientes],
            "medicos": [m.to_dict() for m in self.medicos]
        }
        with open(archivo, "w") as f:
            json.dump(data, f, indent=4)
        print("Datos guardados correctamente.")

    def cargar_datos(self, archivo="hospital.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)

            # Limpiar datos actuales
            self.pacientes = []
            self.medicos = []

            # 1️⃣ Cargar médicos (sin relaciones)
            for m_data in data["medicos"]:
                medico = Medico(
                    m_data["nombre"],
                    m_data["edad"],
                    m_data["genero"],
                    m_data["id_medico"],
                    m_data["especialidad"]
                )
                self.medicos.append(medico)

            # 2️⃣ Cargar pacientes + diagnósticos + citas
            for p_data in data["pacientes"]:
                paciente = Paciente(
                    p_data["nombre"],
                    p_data["edad"],
                    p_data["genero"],
                    p_data["id_paciente"]
                )

                # Diagnósticos
                for diag_data in p_data["historial"]:
                    diag = Diagnostico(
                        diag_data["sintomas"],
                        diag_data["diagnostico"],
                        diag_data["tratamiento"]
                    )
                    diag.fecha = diag_data["fecha"]
                    paciente.agregar_diagnostico(diag)

                # Citas
                for c_data in p_data.get("citas", []):
                    medico = self.buscar_medico(c_data["Medico"])
                    if medico:
                        cita = Cita(medico, c_data["Fecha_hora"])
                        paciente.citas.append(cita)

                self.pacientes.append(paciente)

            # 3️⃣ Reconectar pacientes con médicos
            for m_data in data["medicos"]:
                medico = self.buscar_medico(m_data["id_medico"])
                for pid in m_data.get("pacientes", []):
                    paciente = self.buscar_paciente(pid)
                    if medico and paciente:
                        medico.agregar_paciente(paciente)

            print("Datos cargados correctamente.")

        except FileNotFoundError:
            print("Archivo de datos no encontrado. Se iniciará con hospital vacío.")