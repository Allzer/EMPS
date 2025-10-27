#TODO добавить везде время отправления datetime, добавить название системы


EMPS_STRYCTYRE = {
  # Метка времени генерации данных
  "timestamp": "2024-05-22T14:30:00Z",
  
  # Массив устройств верхнего уровня (цехи, главные станки)
  "devices": [
    {
      # 1. Основная информация об устройстве
      "device_name": "Токарно-фрезерный станок ЧПУ 'Вектор-5000'",
      "device_id": "stank_vector_5000_001",
      "device_type": "cnc_machine", # Тип для удобства группировки и фильтрации
      "serial_number": "V5K-2024-001",

      # 2. Состояние устройства (текущий режим работы)
      "state": [
        {
          "code": 200,
          "name": "В работе",
          "description": "Станок выполняет программу №12345"
        },
        {
          "code": 50,
          "name": "Подача охлаждающей жидкости",
          "description": "Активная система охлаждения"
        }
      ],

      # 3. Текущие ошибки и предупреждения
      "errors": [
        {
          "code": 3001,
          "name": "Предупреждение: Износ инструмента",
          "severity": "warning", # Уровень серьезности: info, warning, error, critical
          "timestamp": "2024-05-22T14:25:00Z"
        }
      ],

      # 5. Части устройства (рекурсивная структура)
      "parts": [
        {
          "device_name": "Основной шпиндель",
          "device_id": "spindle_main_001",
          "device_type": "spindle",
          "state": [
            {
              "code": 1,
              "name": "Вращение",
              "description": "Шпиндель вращается с заданной скоростью"
            }
          ],
          "parts": [] # У шпинделя могут быть свои части (подшипники, датчики), но здесь оставим пусто
        },
        {
          "device_name": "Система подачи охлаждающей жидкости",
          "device_id": "coolant_system_001",
          "device_type": "coolant_system",
          "state": [
            {
              "code": 10,
              "name": "Включена",
              "description": "Циркуляция охлаждающей жидкости активна"
            }
          ],
          "errors": [
            {
              "code": 7002,
              "name": "Сработал фильтр предварительной очистки",
              "severity": "info",
              "timestamp": "2024-05-22T10:15:00Z"
            }
          ],
          "parts": [
            {
              "device_name": "Датчик давления СОЖ",
              "device_id": "sensor_coolant_pressure_001",
              "device_type": "sensor",
            }
          ]
        }
      ]
    },

    # Второе устройство верхнего уровня (например, измерительная стойка)
    {
      "device_name": "Координатно-измерительная машина 'Точность-3D'",
      "device_id": "cmm_precision_3d_001",
      "device_type": "measurement_machine",
      "serial_number": "C3D-2024-002",

      "state": [
        {
          "code": 100,
          "name": "Калибровка",
          "description": "Выполняется самокалибровка по эталону"
        }
      ],

      "errors": [],

      "parts": [
        {
          "device_name": "Контрольная лампа 'Готов'",
          "device_id": "lamp_ready_001",
          "device_type": "indicator_lamp",
          "state": [
            {
              "code": 1,
              "name": "Включена",
              "description": "Лампа горит зеленым цветом"
            }
          ]
        }
      ]
    }
  ]
}