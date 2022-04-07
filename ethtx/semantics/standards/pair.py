#  Copyright 2021 DAI Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from ethtx.models.semantics_model import (
    EventSemantics,
    ParameterSemantics,
    TransformationSemantics,
    FunctionSemantics,
)

pair_sync_event = EventSemantics(
    signature="0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1",
    anonymous=False,
    name="Sync",
    parameters=[
        ParameterSemantics(
            parameter_name="reserve0", parameter_type="uint112", indexed=False
        ),
        ParameterSemantics(
            parameter_name="reserve1", parameter_type="uint112", indexed=False
        ),
    ],
)


pair_swap_function = FunctionSemantics(
    signature="0x022c0d9f",
    name="swap",
    inputs=[
        ParameterSemantics(parameter_name="amount0Out", parameter_type="uint256"),
        ParameterSemantics(parameter_name="amount1Out", parameter_type="uint256"),
        ParameterSemantics(parameter_name="to", parameter_type="address"),
        ParameterSemantics(parameter_name="data", parameter_type="bytes"),
    ],
    outputs=[],
)


PAIR_EVENTS = {pair_sync_event.signature: pair_sync_event}

PAIR_FUNCTIONS = {pair_swap_function.signature: pair_swap_function}

