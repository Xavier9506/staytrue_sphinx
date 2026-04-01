SDC-LE-01D
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SDC-LE-01的插件版本，采用32位高性能RISC核心，优化了封装设计，支持直接插件安装，适合快速原型开发和小批量生产。同时具备宽电压输入特性，支持3.0V~5.5V供电（典型5V），串口支持3V/5V电平兼容，可直接与不同电平的MCU通信，无需额外电平转换电路。

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - .. image:: ../images/sdc-le-01d-img1.png
         :width: 200
         :alt: SDC-LE-01D 模组正面图
     - .. image:: ../images/sdc-le-01d-img2.png
         :width: 200
         :alt: SDC-LE-01D 模组反面图

.. image:: ../images/sdc-le-01d-img3.png
   :width: 500
   :align: center
   :alt: SDC-LE-01D 模组尺寸图

核心性能
~~~~~~~~~~
- 处理器: 32位高性能RISC核心,16MHz时钟
- 存储: 512KB Flash + 40KB SRAM
- 蓝牙射频: 2.4GHz BLE5.0,-97dBm接收灵敏度,输出功率-20~+7dBm可编程
- 电源特性: 宽电压输入范围,支持3.0V~5.5V供电(典型5V),具备过压保护机制
- 串口特性: 支持3V/5V电平兼容,可直接与不同电平的MCU通信,无需额外电平转换电路
- 认证: SRRC、FCC、BQB、NCC
- 工作温度：-40℃ ~ +105℃
- 封装尺寸: 31.4x20.5mm(插件接口)

关键引脚定义
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 关键引脚定义
   :widths: 15 20 45 20
   :header-rows: 1

   * - 引脚
     - 信号名
     - 描述
     - 引脚类型
   * - TX
     - UART_TX
     - 串口TX数据发送端
     - O（输出）
   * - RX
     - UART_RX
     - 串口RX数据接收端
     - I（输入）
   * - G
     - GND
     - 模块地
     - P（电源）
   * - 5V
     - VCC
     - 电源正极，3~5.5V（典型5V）
     - P（电源）