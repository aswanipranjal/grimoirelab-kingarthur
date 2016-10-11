# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#     Santiago Dueñas <sduenas@bitergia.com>
#     Alvaro del Castillo San Felix <acs@bitergia.com>
#

import logging

from datetime import datetime


logger = logging.getLogger(__name__)


class Task:
    """Basic class to store information about a task.

    This class stores the basic information needed to retrieve data
    from a repository. The parameters needed to run the backend
    are given in the dictionary `backend_args`. Other parameters
    can also given to configure the cache (with `cache_args`) or to
    define how this task will be scheduled (with `sched_args`).

    The task will be identified by the `task_id` attribute.

    :param task_id: identifier of this task
    :param backend: backend used to fetch data from the repository
    :param backend_args: dict of arguments required to run the backend
    :param cache_args: dict of arguments to configure the cache, if needed
    :param sched_args: dict of arguments to configure the scheduler, if needed
    """
    def __init__(self, task_id, backend, backend_args,
                 cache_args=None, sched_args=None):
        self._task_id = task_id
        self.created_on = datetime.now().timestamp()
        self.backend = backend
        self.backend_args = backend_args
        self.cache_args = cache_args if cache_args else {}
        self.sched_args = sched_args if sched_args else {}

    @property
    def task_id(self):
        return self._task_id

    def to_dict(self):
        return {
            'task_id' : self.task_id,
            'created_on' : self.created_on,
            'backend' : self.backend,
            'backend_args' : self.backend_args,
            'cache' : self.cache_args,
            'scheduler' : self.sched_args
        }