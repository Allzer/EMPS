from datetime import datetime

#TODO упростить структуру
EMPS_STRYCTYRE = {"timestamp": datetime.now().isoformat() + "Z",
        "system_name": "Производственный мониторинг v2.0",
        "devices": [
            {
                "device_name": "Токарно-фрезерный станок ЧПУ 'Вектор-5000",
                "device_id": "stank_vector_5000_001",
                "device_type": "cnc_machine",
                "serial_number": "V5K-2024-001",
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
                "errors": [
                    {
                        "code": 3001,
                        "name": "Предупреждение: Износ инструмента",
                        "severity": "warning",
                        "timestamp": datetime.now().isoformat() + "Z"
                    }
                ],
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
                        "parts": []
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
                                "timestamp": datetime.now().replace(hour=10, minute=15).isoformat() + "Z"
                            }
                        ],
                        
                    },
                    {
                        "device_name": "Датчик давления СОЖ",
                        "device_id": "sensor_coolant_pressure_001",
                        "device_type": "sensor",
                    }
                ]
            },
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
            },
            {
                "device_name": "Роботизированный сварочный комплекс 'Аргон-M'",
                "device_id": "welder_argon_m_001",
                "device_type": "welding_robot",
                "serial_number": "WAM-2024-003",
                "state": [
                    {
                        "code": 210,
                        "name": "Сварка детали",
                        "description": "Выполняется сварка корпуса изделия АБ-123"
                    },
                    {
                        "code": 75,
                        "name": "Подача защитного газа",
                        "description": "Аргон подается под давлением 0.5 МПа"
                    }
                ],
                "errors": [
                    {
                        "code": 4501,
                        "name": "Низкий уровень газа",
                        "severity": "warning",
                        "timestamp": datetime.now().replace(hour=13, minute=20).isoformat() + "Z"
                    }
                ],
                "parts": [
                    {
                        "device_name": "Сварочная горелка",
                        "device_id": "welding_torch_001",
                        "device_type": "welding_torch",
                        "state": [
                            {
                                "code": 25,
                                "name": "Активна",
                                "description": "Ток: 180А, напряжение: 22В"
                            }
                        ],
                    },    
                    {
                        "device_name": "Датчик температуры горелки",
                        "device_id": "sensor_torch_temp_001",
                        "device_type": "temperature_sensor",
                        "state": [
                            {
                                "code": 1,
                                "name": "Норма",
                                "description": "Температура в пределах нормы: 45°C"
                            }
                        ]
                    },
                    {
                        "device_name": "Система позиционирования",
                        "device_id": "positioning_system_001",
                        "device_type": "positioning_system",
                        "state": [
                            {
                                "code": 15,
                                "name": "Точное позиционирование",
                                "description": "Погрешность: ±0.1 мм"
                            }
                        ]
                    }
                ]
            },
            {
                "device_name": "Ленточный конвейер 'Транспорт-500'",
                "device_id": "conveyor_transport_500_001",
                "device_type": "conveyor",
                "serial_number": "CT5-2024-004",
                "state": [
                    {
                        "code": 180,
                        "name": "Транспортировка",
                        "description": "Скорость ленты: 2.5 м/мин"
                    }
                ],
                "errors": [
                    {
                        "code": 5203,
                        "name": "Предупреждение: Натяжение ленты",
                        "severity": "warning",
                        "timestamp": datetime.now().replace(hour=11, minute=45).isoformat() + "Z"
                    }
                ],
                "parts": [
                    {
                        "device_name": "Приводной двигатель",
                        "device_id": "conveyor_motor_001",
                        "device_type": "electric_motor",
                        "state": [
                            {
                                "code": 30,
                                "name": "Работа",
                                "description": "Обороты: 1450 об/мин, ток: 4.2А"
                            }
                        ],
                        "errors": [
                            {
                                "code": 6101,
                                "name": "Повышенная температура",
                                "severity": "info",
                                "timestamp": datetime.now().replace(hour=14, minute=10).isoformat() + "Z"
                            }
                        ]
                    },
                    {
                        "device_name": "Система датчиков положения",
                        "device_id": "position_sensors_001",
                        "device_type": "sensor_system",
                        "parts": [
                            {
                                "device_name": "Фотоэлектрический датчик",
                                "device_id": "photo_sensor_001",
                                "device_type": "sensor",
                                "state": [
                                    {
                                        "code": 1,
                                        "name": "Активен",
                                        "description": "Контроль прохождения деталей"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "device_name": "Термопластавтомат 'Пласт-300'",
                "device_id": "injection_molder_plast_300_001",
                "device_type": "injection_molding",
                "serial_number": "IP3-2024-005",
                "state": [
                    {
                        "code": 220,
                        "name": "Литье под давлением",
                        "description": "Цикл литья: 45 сек, температура: 240°C"
                    }
                ],
                "errors": [],
                "parts": [
                    {
                        "device_name": "Нагревательный блок",
                        "device_id": "heating_block_001",
                        "device_type": "heating_system",
                        "state": [
                            {
                                "code": 40,
                                "name": "Нагрев",
                                "description": "Температура цилиндра: 235°C"
                            }
                        ],
                    },
                    {
                        "device_name": "ТЭН цилиндра",
                        "device_id": "heater_cartridge_001",
                        "device_type": "heater",
                        "state": [
                            {
                                "code": 5,
                                "name": "Включен",
                                "description": "Мощность: 85%"
                            }
                        ]
                    },
                    {
                        "device_name": "Гидравлическая система",
                        "device_id": "hydraulic_system_001",
                        "device_type": "hydraulic_system",
                        "state": [
                            {
                                "code": 35,
                                "name": "Рабочее давление",
                                "description": "Давление: 120 бар"
                            }
                        ],
                        "errors": [
                            {
                                "code": 7205,
                                "name": "Информация: Замена фильтра",
                                "severity": "info",
                                "timestamp": datetime.now().replace(hour=9, minute=30).isoformat() + "Z"
                            }
                        ]
                    }
                ]
            },
            {
                "device_name": "Лазерный резак 'Луч-Про'",
                "device_id": "laser_cutter_luch_pro_001",
                "device_type": "laser_cutter",
                "serial_number": "LCP-2024-006",
                "state": [
                    {
                        "code": 190,
                        "name": "Резка металла",
                        "description": "Резка листа нержавеющей стали 3мм"
                    }
                ],
                "errors": [
                    {
                        "code": 3802,
                        "name": "Требуется очистка линз",
                        "severity": "warning",
                        "timestamp": datetime.now().replace(hour=15, minute=20).isoformat() + "Z"
                    }
                ],
                "parts": [
                    {
                        "device_name": "Лазерная головка",
                        "device_id": "laser_head_001",
                        "device_type": "laser_head",
                        "state": [
                            {
                                "code": 20,
                                "name": "Излучение",
                                "description": "Мощность лазера: 2.5 кВт"
                            }
                        ],
                    },
                    {
                        "device_name": "Система фокусировки",
                        "device_id": "focus_system_001",
                        "device_type": "optical_system",
                        "state": [
                            {
                                "code": 8,
                                "name": "Автофокус",
                                "description": "Фокусное расстояние: 127.5 мм"
                            }
                        ]
                    },
                    {
                        "device_name": "Система охлаждения лазера",
                        "device_id": "laser_cooling_001",
                        "device_type": "cooling_system",
                        "state": [
                            {
                                "code": 12,
                                "name": "Циркуляция",
                                "description": "Температура воды: 18°C"
                            }
                        ]
                    }
                ]
            },
            {
                "device_name": "Автоматический складской погрузчик",
                "device_id": "agv_loader_001",
                "device_type": "agv",
                "serial_number": "AGV-2024-007",
                "state": [
                    {
                        "code": 170,
                        "name": "Перемещение с грузом",
                        "description": "Маршрут: зона А -> зона Б, груз: 450кг"
                    }
                ],
                "errors": [
                    {
                        "code": 8901,
                        "name": "Слабый сигнал навигации",
                        "severity": "info",
                        "timestamp": datetime.now().replace(hour=14, minute=55).isoformat() + "Z"
                    }
                ],
                "parts": [
                    {
                        "device_name": "Навигационная система",
                        "device_id": "navigation_system_001",
                        "device_type": "navigation",
                        "state": [
                            {
                                "code": 60,
                                "name": "SLAM навигация",
                                "description": "Точность позиционирования: ±5 мм"
                            }
                        ]
                    },
                    {
                        "device_name": "Лидар",
                        "device_id": "lidar_001",
                        "device_type": "sensor",
                        "state": [
                            {
                                "code": 1,
                                "name": "Сканирование",
                                "description": "Частота: 15 Гц"
                            }
                        ]
                    },
                    {
                        "device_name": "Подъемный механизм",
                        "device_id": "lifting_mechanism_001",
                        "device_type": "lifting_system",
                        "state": [
                            {
                                "code": 45,
                                "name": "Поднят",
                                "description": "Высота подъема: 1.2 метра"
                            }
                        ]
                    }
                ]
            }
        ]
    }