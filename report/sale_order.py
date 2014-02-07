from report import report_sxw
import time

# this bit is basically a copy of the stuff
# in the regular sale order module.
# I can't just import that code because it causes
# the sale.order report to get registered again
# causing it to complain.
# otherwise Id do this - from addons.sale.report import order
class order(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(order, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'show_discount':self._show_discount,
        })

    def _show_discount(self, uid, context=None):
        cr = self.cr
        try:
            group_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'sale', 'group_discount_per_so_line')[1]
        except:
            return False
        return group_id in [x.id for x in self.pool.get('res.users').browse(cr, uid, uid, context=context).groups_id]


report_sxw.report_sxw('report.sale.order_extra', 'sale.order', 'addons/openerp-extra-reports/report/sale_order.rml', parser=order, header="external")
